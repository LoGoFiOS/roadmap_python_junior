from typing import List


class Repo:
    print("hello from class")

    def __init__(self, conn):
        self.conn = conn

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num + 1}" for num, item in enumerate(parameters)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, user_id, user_name, user_email: str = 'None') -> None:
        """Store user in DB, ignore duplicates"""
        await self.conn.execute(
            "INSERT INTO users(id, name, email) VALUES($1, $2, $3) ON CONFLICT DO NOTHING",
            user_id, user_name, user_email)
        return

    async def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = f"SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.conn.fetchrow(sql, *parameters)

    async def show_db(self):
        return await self.conn.fetch(
            "SELECT * FROM Users"
        )




    # async def list_users(self) -> List[int]:
    #     """List all bot users"""
    #     return [
    #         # row[0]
    #         # async for row in self.conn.execute(
    #         #     "select userid from tg_users",
    #         # )
    #     ]

#

#
#     async def count_users(self):
#         return await self.pool.fetchval("SELECT COUNT(*) FROM Users")
#
#     async def update_user_email(self, email, id):
#         # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"
#
#         sql = f"""
#         UPDATE Users SET email=$1 WHERE id=$2
#         """
#         return await self.pool.execute(sql, email, id)
