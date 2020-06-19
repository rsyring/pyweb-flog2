from flask.testing import FlaskCliRunner


class CLIRunner(FlaskCliRunner):
    def invoke(self, *args, **kwargs):
        # Letting Click catch the exception makes it harder to troubleshoot, just let the
        # exception surface.
        kwargs.setdefault('catch_exceptions', False)
        # assign invoke's args to the args variable to give better ergonomics.  i.e.:
        # invoke('foo', 'bar') vs invoke(args=('foo', 'bar'))
        return super().invoke(None, args, **kwargs)
