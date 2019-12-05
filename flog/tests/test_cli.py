from unittest import mock


class TestCLI:

    def test_hn_profile(self, app):
        runner = app.test_cli_runner()

        result = runner.invoke(args=['hn-profile', 'rsyring'], catch_exceptions=False)
        assert 'HackerNews user rsyring has 98 submissions and 394 karma.\n' == result.output

    @mock.patch('flog.libs.hackernews.User.get_json', autospec=True, spec_set=True)
    def test_hn_profile_mock(self, m_get_json, app):
        m_get_json.return_value = {'karma': 123, 'submitted': [1, 2, 3]}

        runner = app.test_cli_runner()

        result = runner.invoke(args=['hn-profile', 'rsyring'], catch_exceptions=False)
        assert 'HackerNews user rsyring has 3 submissions and 123 karma.\n' == result.output
