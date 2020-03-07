import concurrent.futures

import arrow
import click
import dramatiq
from flask import Blueprint

from flog import actors
from flog.libs import hackernews as hn
from flog.libs import localhost


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


@cli_bp.cli.command()
@click.option('--queue', 'use_queue', is_flag=True, default=False)
def falcon_page(use_queue):
    if use_queue:
        actors.falcon_page.send()
        print('random_article() job has been queued.')
    else:
        print(actors.falcon_page())


@cli_bp.cli.command()
@click.argument('fetch_number', default=10)
def falcon_pages(fetch_number):
    page_messages = [actors.falcon_page.message() for x in range(fetch_number)]
    group = dramatiq.group(page_messages).run()
    # 60 second timeout (in milliseconds)
    for result in group.get_results(block=True, timeout=60_000):
        print(result)


@cli_bp.cli.command()
@click.argument('requests_num', type=int)
@click.option('--workers-num', default=5)
def falcon_pages_threadpool(workers_num, requests_num):
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers_num) as executor:
        future_to_url = [executor.submit(localhost.fetch_page) for x in range(requests_num)]

    start = arrow.now()
    for future in concurrent.futures.as_completed(future_to_url):
        print(future.result())

    duration = arrow.now() - start
    secs = duration.total_seconds()

    print('worker count:', workers_num)
    print('Requests / second:', requests_num / secs)


@cli_bp.cli.command()
@click.argument('requests_num', type=int)
@click.option('--workers-num', default=4)
def falcon_pages_procpool(workers_num, requests_num):
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers_num) as executor:
        future_to_url = [executor.submit(localhost.fetch_page) for x in range(requests_num)]

    start = arrow.now()
    for future in concurrent.futures.as_completed(future_to_url):
        print(future.result())

    duration = arrow.now() - start
    secs = duration.total_seconds()

    print('worker count:', workers_num)
    print('Requests / second:', requests_num / secs)


@cli_bp.cli.command()
@click.argument('requests_num', type=int)
@click.option('--workers-num', default=4)
def falcon_pages_async(workers_num, requests_num):
    import aiohttp
    import asyncio

    async def fetch(session, url):
        async with session.get(url) as response:
            return await response.text()

    async def main():
        async with aiohttp.ClientSession() as session:
            for x in range(requests_num):
                text = await fetch(session, 'http://localhost:5000/')
                print(text)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
