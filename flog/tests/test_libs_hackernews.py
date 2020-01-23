import responses

from flog.libs import hackernews as hn


class TestHackerNews:

    @responses.activate
    def test_web_request(self):
        responses.add(
            responses.GET,
            'https://hacker-news.firebaseio.com/v0/user/rsyring.json',
            json={'karma': 123, 'submitted': [1, 2, 3]}
        )
        rsyring = hn.User('rsyring')
        assert rsyring.karma == 123
        assert rsyring.subcount == 3

    def test_data_param(self):
        rsyring = hn.User('rsyring', _user_data={'karma': 123, 'submitted': [1, 2, 3]})
        assert rsyring.karma == 123
        assert rsyring.subcount == 3
