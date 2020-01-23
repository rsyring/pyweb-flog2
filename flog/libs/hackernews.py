import contextlib

from unittest import mock

import requests


def top_stories():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    return requests.get(url).json()


def story(story_id):
    url = f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json'
    return requests.get(url).json()


class User:

    def __init__(self, username, _user_data=None):
        self.username = username
        self.json = _user_data or self.get_json(username)
        self.karma = self.json['karma']
        self.subcount = len(self.json['submitted'])

    def get_json(self, username):
        url = 'https://hacker-news.firebaseio.com/v0/user/{}.json'.format(username)
        resp = requests.get(url)
        user_json = resp.json()
        if user_json is None:
            return None
        return user_json

    def __str__(self):
        return f'HackerNews user {self.username} has {self.subcount} submissions and' \
            f' {self.karma} karma.'


@contextlib.contextmanager
def mock_user(**kwargs):
    with mock.patch('flog.libs.hackernews.User.get_json', autospec=True, spec_set=True) \
            as m_get_json:
        m_get_json.return_value = kwargs
        yield
