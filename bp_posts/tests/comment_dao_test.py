import pytest

from bp_posts.dao.comment_dao import CommentDAO

class TestCommentDAO:

    ###Функция получения комментариев по его pk

    @pytest.fixture
    def comment_dao(self):
        comment_dao_instance = CommentDAO('./bp_posts/tests/comment_mock.json')
        return comment_dao_instance

    def test_get_comments_by_post_id_type(self, comment_dao):
        comments = comment_dao.get_comments_by_post_id(111)
        assert type(comments) == list, 'Incorrect type for result'

    def test_get_comments_by_post_id_none(self, comment_dao):
        comment = comment_dao.get_comments_by_post_id(111)
        assert comment == [], 'Должно быть []'
