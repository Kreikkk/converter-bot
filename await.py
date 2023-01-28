import asyncio
import asyncpg
import settings
from time import sleep

host = settings.DB_HOST
port = settings.DB_PORT

async def main():
    while True:
        print(f'Waiting Postgres to launch on {host}:{port}')
        try:
            conn = await asyncpg.connect(
                host=host,
                port=port,
                database=settings.DB_NAME,
                user=settings.DB_USER,
                password=settings.DB_PASSWORD
            )
            break
        except Exception as ex:
            sleep(1.5)

asyncio.get_event_loop().run_until_complete(main())