import json


class PostsJson:

    def __init__(self, path):
        self.path = path

    def _load_posts(self):
        """Загружаем список всех постов"""
        with open(self.path, 'r', encoding='utf-8') as file:
            posts = json.load(file)
        return posts

    def get_all_posts(self):
        """Возвращаем все посты"""
        posts = self._load_posts()
        return posts

    def get_post_by_pk(self, pk):
        """Возвращает один пост по его идентификатору (pk)"""
        posts = self.get_all_posts()
        for post in posts:
            if post['pk'] == pk:
                return post