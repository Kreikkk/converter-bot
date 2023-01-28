from sqlalchemy.ext.asyncio import create_async_engine

import settings


class Connector:
    def __init__(self):
        self.host = settings.DB_HOST
        self.port = settings.DB_PORT
        self.dbname = settings.DB_NAME
        self.user = settings.DB_USER
        self.password = settings.DB_PASSWORD
        self.uri = f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"
        self.engine = create_async_engine(self.uri, echo=settings.LOG_SQL, pool_size=5, max_overflow=10)

    def connect(self):
        return self.engine.begin()