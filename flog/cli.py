import click
from flask import Blueprint

from flog.libs import hackernews as hn

cli_bp = Blueprint('cli', __name__, cli_group=None)


@cli_bp.cli.command('hn-profile')
@click.argument('username')
def hn_profile(username):
    user = hn.User(username)
    print(f'HackerNews user {username} has {user.subcount} submissions and {user.karma} karma.')
