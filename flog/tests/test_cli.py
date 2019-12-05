from flog.libs import hackernews


class TestCLI:

    def test_hn_profile(self, app):
        with hackernews.mock_user(karma=123, submitted=[1, 2, 3]):
            runner = app.test_cli_runner()

            result = runner.invoke(args=['hn-profile', 'rsyring'], catch_exceptions=False)
            assert 'HackerNews user rsyring has 3 submissions and 123 karma.\n' == result.output
