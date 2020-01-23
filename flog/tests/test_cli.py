from unittest import mock

import responses


class TestCLI:

    @responses.activate
    def test_requests_mock(self, app):
        responses.add(
            responses.GET,
            'https://hacker-news.firebaseio.com/v0/user/rsyring.json',
            json={'karma': 394, 'submitted': [1, 2, 3]}
        )

        runner = app.test_cli_runner()

        result = runner.invoke(args=['hn-profile', 'rsyring'], catch_exceptions=False)
        assert 'HackerNews user rsyring has 3 submissions and 394 karma.\n' == result.output

    @mock.patch('flog.libs.hackernews.User.get_json', autospec=True, spec_set=True)
    def test_library_mock(self, m_get_json, app):
        m_get_json.return_value = {'karma': 123, 'submitted': [1, 2, 3]}

        runner = app.test_cli_runner()

        result = runner.invoke(args=['hn-profile', 'rsyring'], catch_exceptions=False)
        assert 'HackerNews user rsyring has 3 submissions and 123 karma.\n' == result.output
