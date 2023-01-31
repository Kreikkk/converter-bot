from sqlalchemy import select, insert, update
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    @classmethod
    async def filter(cls, conn, *filter_):
        return await conn.execute(select(cls).filter(*filter_))

    @classmethod
    async def create(cls, conn, **filter_):
        return await conn.execute(insert(cls).values(**filter_))

    @classmethod
    async def update(cls, conn, *filter_, **values):
        return await conn.execute(update(cls).filter(*filter_).values(**values))

    @classmethod
    def filter_pre(cls, *filter_):
        return select(cls).filter(*filter_)
    
    @classmethod
    def update_pre(cls, *filter_, **values):
        return update(cls).filter(*filter_).values(**values)
