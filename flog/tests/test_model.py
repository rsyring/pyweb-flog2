from flog.model import entities as ents


class TestPost:

    def test_insert(self, mixer):
        mixer.blend(ents.Post)
        assert ents.Post.query.count() == 1
        post = ents.Post.query.one()
        print(post)


class TestComment:

    def test_insert(self, mixer):
        mixer.blend(ents.Comment)
        assert ents.Comment.query.count() == 1
        comment = ents.Comment.query.one()
        print(comment)
        print(comment.post)

    def test_count(self, mixer):
        ents.Post.query.delete()
        mixer.blend(ents.Comment)
        assert ents.Comment.query.count() == 1
