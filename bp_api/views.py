from flask import jsonify, Blueprint


from bp_api.posts_json import PostsJson
from logger import logger

api_blueprint = Blueprint('api_blueprint', __name__, template_folder='templates')

path_post = 'data/data.json'
posts = PostsJson(path_post)


@api_blueprint.route('/api/posts')
def read_posts():
    all_posts = posts.get_all_posts()
    logger.info('Запрос /api/posts')
    return jsonify(all_posts)

@api_blueprint.route('/api/posts/<int:post_id>')
def read_posts_pk(post_id):
    post = posts.get_post_by_pk(post_id)
    logger.info(f'Запрос /api/posts{post_id}')
    return jsonify(post)
