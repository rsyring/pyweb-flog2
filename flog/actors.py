import dramatiq

import flog.libs.dramatiq
from flog.libs.hackernews import story
from flog.libs import wikipedia
from flog.libs import localhost

flog.libs.dramatiq.configure()


@dramatiq.actor
def say_hello(name):
    print(f'Hello {name}!')


@dramatiq.actor(store_results=True, min_backoff=50, max_backoff=250)
def hn_story(story_id):
    story_data = story(story_id)
    title = story_data['title']
    author = story_data['by']
    return(f'"{title}" by {author}')


@dramatiq.actor(store_results=True, min_backoff=50, max_backoff=250)
def random_article():
    response = wikipedia.random_article()
    article = response['items'][0]
    title = article['title']
    author = article['user_text']
    return(f'"{title}" by {author}')


@dramatiq.actor(store_results=True, min_backoff=50, max_backoff=250)
def falcon_page():
    return(localhost.fetch_page())
