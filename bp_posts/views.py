from flask import render_template, request, Blueprint
from bp_posts.dao.post_dao import PostDAO
from bp_posts.dao.comment_dao import CommentDAO
from exception import DataError, DataNameError, DataCommError
from logger import logger

path_post = 'data/data.json'
path_comment = 'data/comments.json'

posts = PostDAO(path_post)
comments = CommentDAO(path_comment)
posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')


@posts_blueprint.route('/')
def home_page():
    all_posts = posts.get_all_posts()
    return render_template('index.html', posts=all_posts)


@posts_blueprint.route('/search/')
def search_page():
    s = request.args.get('s', '')
    search_posts = posts.search_in_contents(s)
    return render_template('search.html', posts=search_posts, len=len(search_posts), s=s)


@posts_blueprint.route('/user_post/<username>')
def user_post_page(username):
    user_posts = posts.get_posts_by_user(username)
    return render_template('user-feed.html', posts=user_posts)


@posts_blueprint.route('/post/<int:pk>')
def comment_post_page(pk):
    posts.update_views_count(pk)
    comment_post = comments.get_comments_by_post_id(pk)
    post_pk = posts.get_post_by_pk(pk)
    return render_template('post.html', posts=comment_post, post_pk=post_pk, len=len(comment_post))


@posts_blueprint.route('/bookmarks/')
def bookmarks():
    # return render_template('bookmarks.html')
    return 'Закладки'

@posts_blueprint.errorhandler(DataError)
def data_error(e):
    logger.error("Файл поврежден")
    return "Файл поврежден"


@posts_blueprint.errorhandler(DataNameError)
def data_error(e):
    logger.error("Такого пользователя нет или пустой список")
    return "Файл с данными поврежден"


@posts_blueprint.errorhandler(DataCommError)
def data_error(e):
    logger.error("Такого поста нет")
    return "Такого поста нет"
