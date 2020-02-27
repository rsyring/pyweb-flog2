import click
import dramatiq
from flask import Blueprint

from flog import actors
from flog.libs import hackernews as hn

cli_bp = Blueprint('cli', __name__, cli_group=None)


@cli_bp.cli.command('hn-profile')
@click.argument('username')
def hn_profile(username):
    user = hn.User(username)
    print(user)


@cli_bp.cli.command('hello')
@click.argument('name', default='World')
@click.option('--queue', 'use_queue', is_flag=True, default=False)
def hello(name, use_queue):
    if use_queue:
        actors.say_hello.send(name)
        print('say_hello() job has been queued.')
    else:
        actors.say_hello(name)


@cli_bp.cli.command()
def top_stories():
    story_ids = hn.top_stories()
    messages = [actors.hn_story.message(sid) for sid in story_ids]
    group = dramatiq.group(messages).run()
    # 60 second timeout (in milliseconds)
    for result in group.get_results(block=True, timeout=60_000):
        print(result)
