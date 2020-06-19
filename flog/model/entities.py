from flog.ext import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)

    comments = db.relationship('Comment', lazy=True)

    def __repr__(self):
        return f'<Post ({self.id}): {self.title[0:50]}>'

    @classmethod
    def testing_create(cls, **kwargs):
        post = cls(
            title=kwargs.get('title', 'foo'),
            author=kwargs.get('author', 'bar'),
            body=kwargs.get('body', 'baz'),
        )
        db.session.add(post)
        db.session.commit()
        return post


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)

    post_id = db.Column(db.Integer, db.ForeignKey(Post.id, ondelete='cascade'), nullable=False)
    post = db.relationship(Post)

    def __repr__(self):
        return f'<Comment ({self.id}): {self.title[0:50]}>'

    @classmethod
    def testing_create(cls, **kwargs):
        comment = cls(
            title=kwargs.get('title', 'foo'),
            author=kwargs.get('author', 'bar'),
            body=kwargs.get('body', 'baz'),
            post=kwargs.get('post') or Post.testing_create()
        )
        db.session.add(comment)
        db.session.commit()
        return comment
