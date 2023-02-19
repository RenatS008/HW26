import json
from json import JSONDecodeError

from bp_posts.dao.comment import Comment
from exception import DataError, DataCommError


class CommentDAO:

    def __init__(self, path):
        self.path = path

    def _load_data(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                comments = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataError(f'Файл поврежден {self.path}')
        return comments

    def _load_comments(self):
        """
        Возвращает список экземпляров Comment
        """
        comments_data = self._load_data()
        list_of_comments = [Comment(**comment_data) for comment_data in comments_data]
        return list_of_comments

    def get_comments_by_post_id(self, post_id):
        """Возвращает комментарии определенного поста"""
        comment_post = []
        comments = self._load_comments()
        try:
            for comment in comments:
                if comment.post_id == post_id:
                    comment_post.append(comment)
        except (ValueError):
            raise DataCommError('Такого поста нет')
        return comment_post


