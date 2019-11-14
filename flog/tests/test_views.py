import pytest

from flog.model import entities as ents


class TestViews:
    @pytest.fixture(autouse=True)
    def setup(self, db):
        ents.Post.query.delete()

    def test_hello(self, client):
        resp = client.get('/hello')
        assert resp.data == b'Hello DerbyPy!'

    def test_posts(self, mixer, client):
        mixer.blend(ents.Post, title='Foo Bar')
        resp = client.get('/posts')
        assert resp.data == b'Foo Bar'
