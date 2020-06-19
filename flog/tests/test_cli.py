import subprocess


class TestCLI:

    def test_hello(self, cli):
        result = cli.invoke('hello')
        assert result.output == 'Hello, World!\n'

        result = cli.invoke('hello', 'pyweb')
        assert result.output == 'Hello, pyweb!\n'

    def test_log_level_option(self, script_args):
        # Can't use the runner to test this because pytest hijacks the log output.  So, just
        # fork out a process to call the application like we would in a script.
        args = script_args + ['--debug', 'hello']
        result = subprocess.run(args, capture_output=True)

        assert result.stdout == b'Hello, World!\n', result.stderr
        assert b'DEBUG - flog.cli - cli debug logging example' in result.stderr
