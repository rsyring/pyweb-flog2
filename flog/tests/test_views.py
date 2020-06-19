
class TestViews:

    def test_hello(self, web):
        resp = web.get('/hello')
        assert resp.data == b'Hello DerbyPy!'
