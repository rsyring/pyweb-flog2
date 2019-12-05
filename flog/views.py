from flask import Blueprint, jsonify, request

from flog.libs import hackernews
from flog.model.entities import Post

public = Blueprint('public', __name__)


@public.route('/hello')
def hello():
    return 'Hello DerbyPy!'


@public.route('/posts')
def posts():
    post_titles = [post.title for post in Post.query]
    return '\n'.join(post_titles)


@public.route('/posts-json')
def posts_json():
    post_titles = [post.title for post in Post.query]
    return jsonify({'data': post_titles})


@public.route('/hn', methods=('GET', 'POST'))
def hn():
    if request.method == 'GET':
        return 'Please enter your HackerNews username:'
    else:
        username = request.form['username']
        user = hackernews.User(username)
        return f'HackerNews user {username} has {user.subcount} submissions and {user.karma} karma.'
