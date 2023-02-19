class DataError(Exception):
    """Файл поврежден"""
    pass


class DataNameError(Exception):
    """Такого пользователя нет и пустой список, если у пользователя нет постов"""
    pass

class DataCommError(Exception):
    """Такого поста нет"""
    pass
