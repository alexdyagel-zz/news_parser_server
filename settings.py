import os
from dotenv import load_dotenv

env = load_dotenv()

APP_PORT = os.getenv('APP_PORT')

_POSTGRES_DB_PORT = os.getenv('POSTGRES_PORT')
_POSTGRES_DB_NAME = os.getenv('POSTGRES_DB')
_POSTGRES_DB_LOGIN = os.getenv('POSTGRES_USER')
_POSTGRES_DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
_POSTGRES_DB_ADDRESS = os.getenv('POSTGRES_ADDRESS')


POSTGRES_DB_PATH = (
    f'postgres://{_POSTGRES_DB_LOGIN}:{_POSTGRES_DB_PASSWORD}@'
    f'{_POSTGRES_DB_ADDRESS}:{_POSTGRES_DB_PORT}/{_POSTGRES_DB_NAME}')
