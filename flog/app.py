import logging
import pathlib
from os import environ

import click
import flask
from flask.cli import FlaskGroup

import flog.cli
import flog.ext
from flog.libs.config import init_config
from flog.libs.logging import init_logging
from flog.libs.testing import CLIRunner
import flog.views

_app_name = 'flog'
_root_path = pathlib.Path(__file__).parent

log = logging.getLogger(__name__)


class FlogApp(flask.Flask):
    test_cli_runner_class = CLIRunner

    @classmethod
    def create(cls, init_app=True, testing=False, **kwargs):
        """
            For CLI app init blueprints but not config b/c we want to give the calling CLI group
            the ability to set values from the command line args/options before configuring the
            app. But if we don't init the blueprints right away, then the CLI doesn't know
            anything about the cli groups & commands added by blueprints.
        """
        if testing:
            environ['FLASK_ENV'] = 'testing'

        app = cls(_app_name, root_path=_root_path, **kwargs)
        app.testing = testing

        app.init_blueprints()
        if init_app:
            app.init_app()

        return app

    def init_blueprints(self):
        self.register_blueprint(flog.cli.cli_bp)
        self.register_blueprint(flog.views.public)

    def init_app(self, log_level='info', with_sentry=False):
        init_config(self)

        if not self.testing:
            init_logging(log_level, self.name)

        if with_sentry:
            assert not self.testing, 'Sentry should not be enabled during testing.'
            sentry_dsn = self.config.get('SENTRY_DSN')
            if not sentry_dsn:
                raise ValueError('Sentry DSN expected but not configured.')
            else:
                import sentry_sdk
                sentry_sdk.init(sentry_dsn)

        flog.ext.init_ext(self)


@click.group(cls=FlaskGroup, create_app=lambda _: FlogApp.create(init_app=False))
@click.option('--quiet', 'log_level', flag_value='quiet', help='Hide info level log messages')
@click.option('--info', 'log_level', flag_value='info', default=True,
    help='Show info level log messages (default)')
@click.option('--debug', 'log_level', flag_value='debug', help='Show debug level log messages')
@click.option('--with-sentry', is_flag=True, default=False,
    help='Enable Sentry (usually only in production)')
@flask.cli.pass_script_info
def cli(scriptinfo, log_level, with_sentry):
    app = scriptinfo.load_app()
    app.init_app(log_level, with_sentry)
