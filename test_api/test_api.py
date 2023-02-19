# from bp_api.views import api_blueprint
from app import app


class TestApp:

    def test_app(self):
        response = app.test_client().get('/', follow_redirects=True)
        assert response.status_code == 200

    def test_app_api_posts(self):
        response = app.test_client().get('/api/posts', follow_redirects=True)
        assert response.status_code == 200
        assert type(response.json) == list, 'Ошибка типа данных'

    def test_app_api_posts_id(self):
        response = app.test_client().get('/api/posts/3', follow_redirects=True)
        assert response.status_code == 200
        assert type(response.json) == dict, 'Ошибка типа данных'

    def test_app_api_posts_keys(self):
        posts_keys = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}
        response = app.test_client().get('/api/posts', follow_redirects=True)
        post = response.json[0]
        assert len(post.keys()) == len(posts_keys), 'Ошибка количества ключей'
        assert set(post.keys()) == posts_keys, 'Ошибка в названии ключей'


