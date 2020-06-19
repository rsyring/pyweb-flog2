import datetime as dt
import logging
from logging.handlers import SysLogHandler
import os
import stat

from pythonjsonlogger import jsonlogger

log = logging.getLogger(__name__)

LOG_STDOUT_FORMAT_STR_INFO = '%(message)s'
LOG_STDOUT_FORMAT_STR_DEBUG = '%(levelname)s - %(name)s - %(message)s'


def init_logging(level, appname):
    root_logger = logging.getLogger()

    if level == 'debug':
        minimum_level = logging.DEBUG
    else:
        minimum_level = logging.INFO

    root_logger.setLevel(minimum_level)

    init_stdout_logging(root_logger, level)

    # CI image doesn't have syslog, so trying to initialize it throws an exception.
    if f'{appname.upper()}_SYSLOG_DISABLE' not in os.environ:
        init_syslog_logging(root_logger, minimum_level, appname)


def init_syslog_logging(logger, minimum_level, appname):
    handler = create_syslog_handler()
    handler.setLevel(minimum_level)
    logger.addHandler(handler)

    # A space is needed at the end of the ident so syslog recognizes it as the
    # app name and not part of the message.
    handler.ident = f'{appname} '
    handler.setFormatter(create_json_formatter())
    handler.setLevel(minimum_level)


def init_stdout_logging(logger, level):

    # always show warnings and exceptions
    error_handler = logging.StreamHandler()
    error_handler.setFormatter(logging.Formatter(LOG_STDOUT_FORMAT_STR_DEBUG))
    error_handler.setLevel(logging.WARN)
    logger.addHandler(error_handler)

    if level == 'quiet':
        return

    handler = logging.StreamHandler()
    logger.addHandler(handler)

    # Because we have a handler above that will show warnings and exceptions, this handler
    # should only show messages below those levels or we will get duplicate messages.
    handler.addFilter(BelowWarnings())

    if level == 'info':
        handler.setFormatter(logging.Formatter(LOG_STDOUT_FORMAT_STR_INFO))
        handler.setLevel(logging.INFO)
    elif level == 'debug':
        handler.setFormatter(logging.Formatter(LOG_STDOUT_FORMAT_STR_DEBUG))
        handler.setLevel(logging.DEBUG)


class BelowWarnings(logging.Filter):
    """
        Don't report warnings or above.
    """
    def filter(self, record):
        if record.levelno < logging.WARNING:
            return True


def create_syslog_handler():
    address = find_syslog_address()
    if not address:
        raise Exception('Could not find syslog socket')

    log.debug(f'Using syslog address: {address}')
    return SysLogHandler(address=address)


def find_syslog_address():
    if _is_socket('/var/run/syslog'):
        return '/var/run/syslog'
    if _is_socket('/dev/log'):
        return '/dev/log'


def _is_socket(path):
    if not os.path.exists(path):
        return False
    mode = os.stat(path).st_mode
    return stat.S_ISSOCK(mode)


class JSONFormatter(jsonlogger.JsonFormatter):
    def process_log_record(self, log_record):
        # Log processing providers like logzio often auto-recognize a field labeled "timestamp".
        log_record['timestamp'] = dt.datetime.utcnow().isoformat()
        return log_record


def create_json_formatter():
    format_str = '%(pathname) %(funcName) %(lineno) %(message) %(levelname)' \
        ' %(name)s %(process) %(processName) %(message)'
    # @cee is recognized by logging parsers as a JSON string
    return JSONFormatter(format_str, prefix='@cee:')
