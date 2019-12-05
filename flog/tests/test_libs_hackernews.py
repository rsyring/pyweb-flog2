from flog.libs import hackernews as hn


class TestHackerNews:

    def test_karma(self):
        assert hn.karma('rsyring') == 394

    def test_subcount(self):
        assert hn.subcount('rsyring') == 98


class TestHackerNews2:

    def test_live(self):
        rsyring = hn.User('rsyring')
        assert rsyring.karma == 394
        assert rsyring.subcount == 98

    def test_data(self):
        rsyring = hn.User('rsyring', _user_data={'karma': 123, 'submitted': [1, 2, 3]})
        assert rsyring.karma == 123
        assert rsyring.subcount == 3

    def test_mock(self):
        with hn.mock_user(karma=123, submitted=[1, 2, 3]):
            user = hn.User('foo')
            assert user.karma == 123
            assert user.subcount == 3

    def test_str(self):
        with hn.mock_user(karma=123, submitted=[1, 2, 3]):
            user = hn.User('foo')
            assert f'{user}' == 'HackerNews user foo has 3 submissions and 123 karma.'
