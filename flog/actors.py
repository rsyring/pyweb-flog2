import dramatiq

import flog.libs.dramatiq
from flog.libs.hackernews import story

flog.libs.dramatiq.configure()


@dramatiq.actor
def say_hello(name):
    print(f'Hello {name}!')


@dramatiq.actor(store_results=True, min_backoff=250, max_backoff=5_000)
def hn_story(story_id):
    story_data = story(story_id)
    title = story_data['title']
    author = story_data['by']
    return(f'"{title}" by {author}')
