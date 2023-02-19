import pytest

from bp_posts.dao.post import Post
from bp_posts.dao.post_dao import PostDAO


def check_fields(post):
    fields = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']

    for field in fields:
        assert hasattr(post, field), f'Нет поля {field}'


class TestPostsDAO:

    ###Функция получения всех постов

    @pytest.fixture
    def post_dao(self):
        post_dao_instance = PostDAO('./bp_posts/tests/post_mock.json')
        return post_dao_instance

    def test_get_all_posts_type(self, post_dao):

        posts = post_dao.get_all_posts()
        assert type(posts) == list, 'Incorrect type for result'
        post = post_dao.get_all_posts()[0]
        assert type(post) == Post, 'Incorrect type single result'

    def test_get_all_posts_type_fields(self, post_dao):
        """
        Проверка наличия поля
        """
        post = post_dao.get_all_posts()[0]
        check_fields(post)

    def test_get_all_posts_type_id(self, post_dao):

        posts = post_dao.get_all_posts()
        correct_pk = {1, 2, 3}
        pk = set([post.pk for post in posts])
        assert pk == correct_pk, 'Не совпадают полученные id'

    ###Функция получения поста по его pk

    def test_get_post_by_pk_type(self, post_dao):
        post = post_dao.get_post_by_pk(1)
        assert type(post) == Post, 'Incorrect type single result'

    def test_get_post_by_pk_fields(self, post_dao):
        post = post_dao.get_post_by_pk(1)
        check_fields(post)

    def test_get_post_by_pk_none(self, post_dao):
        post = post_dao.get_post_by_pk(111)
        assert post is None, 'Должно быть None'

    @pytest.mark.parametrize('pk', [1, 2, 3])
    def test_get_post_by_pk(self, post_dao, pk):
        post = post_dao.get_post_by_pk(pk)
        assert post.pk == pk, 'Некорректный pk'

    ###Функция поиска постов по ключевому слову

    def test_search_in_contents_type(self, post_dao):
        posts = post_dao.search_in_contents('на')
        assert type(posts) == list, 'Incorrect type for result'

    def test_search_in_contents_fields(self, post_dao):
        """
        Проверка наличия поля
        """
        post = post_dao.search_in_contents('на')[0]
        check_fields(post)

    def test_search_in_contents_not_found(self, post_dao):
        posts = post_dao.search_in_contents('111')
        assert posts == [], 'Должен быть []'

    @pytest.mark.parametrize('s, pk', [
        ('Ага', {1}),
        ('Вышел', {2}),
        ('на', {1, 2, 3})
    ])
    def test_search_in_contents_results(self, post_dao, s, pk):
        posts = post_dao.search_in_contents(s)
        pks = set(post.pk for post in posts)
        assert pks == pk, f'Некоректный поиск {s}'

    ###Функция получения списка постов по имени автора поста

    def test_get_posts_by_user_type(self, post_dao):
        posts = post_dao.get_posts_by_user('hank')
        assert type(posts) == list, 'Incorrect type for result'

    def test_get_posts_by_user_not_found(self, post_dao):
        posts = post_dao.search_in_contents('hank')
        assert posts == [], 'Должен быть []'
