from flog.model import entities as ents


class TestPost:

    def test_insert(self, db):
        post = ents.Post.testing_create()
        assert ents.Post.query.count() == 1
        assert ents.Post.query.first() is post


class TestComment:

    def test_insert(self, db):
        comment = ents.Comment.testing_create()
        assert ents.Comment.query.count() == 1
        assert ents.Comment.query.first() is comment
