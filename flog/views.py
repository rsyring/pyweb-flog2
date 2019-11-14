from flask import Blueprint

from flog.model.entities import Post

public = Blueprint('public', __name__)


@public.route('/hello')
def hello():
    return 'Hello DerbyPy!'


@public.route('/posts')
def posts():
    post_titles = [post.title for post in Post.query]
    return '\n'.join(post_titles)
