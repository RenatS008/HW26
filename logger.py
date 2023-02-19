import logging

logger = logging.getLogger('logger')
logger.setLevel('DEBUG')
file_handler = logging.FileHandler('logs/api.log', encoding="utf-8")
formatter = logging.Formatter(fmt='%(asctime)s [%(levelname)s] %(message)s')
logger.addHandler(file_handler)
file_handler.setFormatter(formatter)