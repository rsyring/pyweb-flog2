import contextlib

from unittest import mock

import requests


def karma(username):
    url = 'https://hacker-news.firebaseio.com/v0/user/{}.json'.format(username)
    resp = requests.get(url)
    user_json = resp.json()
    if user_json is None:
        return None
    return user_json['karma']


def subcount(username):
    url = 'https://hacker-news.firebaseio.com/v0/user/{}.json'.format(username)
    resp = requests.get(url)
    user_json = resp.json()
    if user_json is None:
        return None
    return len(user_json['submitted'])


class User:

    def __init__(self, username, _user_data=None):
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


@contextlib.contextmanager
def mock_user(**kwargs):
    with mock.patch('flog.libs.hackernews.User.get_json', autospec=True, spec_set=True) \
            as m_get_json:
        m_get_json.return_value = kwargs
        yield
