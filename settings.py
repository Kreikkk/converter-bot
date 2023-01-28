import logging

from environs import Env
from sqlalchemy import MetaData

logging.basicConfig(level=logging.DEBUG)

metadata = MetaData()

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')

DB_HOST = env('DB_HOST')
DB_PORT = env.int('DB_PORT')
DB_NAME = env('DB_NAME')
DB_USER = env('DB_USER')
DB_PASSWORD = env('DB_PASSWORD')

LOG_SQL = env.bool('LOG_SQL')
