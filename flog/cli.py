import logging

import click
from flask import Blueprint, current_app

from flog.libs.database import create_db

log = logging.getLogger(__name__)
cli_bp = Blueprint('cli', __name__, cli_group=None)


@cli_bp.cli.command()
@click.argument('name', default='World')
def hello(name):
    log.debug('cli debug logging example')
    print(f'Hello, {name}!')


@cli_bp.cli.command()
@click.option('--drop-first', is_flag=True, default=False)
@click.option('--for-tests', is_flag=True, default=False)
def db_init(drop_first, for_tests):
    """ Initialize the database """
    app = current_app
    sa_url = app.config['SQLALCHEMY_DATABASE_URI']
    if for_tests:
        sa_url += '_tests'

    create_db(sa_url, drop_first)
