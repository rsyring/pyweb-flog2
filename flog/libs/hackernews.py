import requests


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
