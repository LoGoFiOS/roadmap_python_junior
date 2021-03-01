from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from bot.db.repository import Repo


class DbMiddleware(LifetimeControllerMiddleware):
    def __init__(self, pool):
        super().__init__()
        self.pool = pool
        # print("hello from MW init")

    async def pre_process(self, obj, data, *args):
        con = await self.pool.acquire() # not recommended!!!
        # print("hello from pre_process")
        data["conn"] = con
        data["repo"] = Repo(con)

    async def post_process(self, obj, data, *args):
        # print("hello from post_process")
        conn = data.get("conn")
        await self.pool.release(conn)
