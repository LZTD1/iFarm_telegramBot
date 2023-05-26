import asyncpg, asyncio, time, asyncio


class database:
    async def query_dict(self, query):
        try:
            results = await self.conn.fetch(query)
            col_names = results[0].keys()
            return [dict(row.items()) for row in results]
        except IndexError:
            return False
    async def connect(self, uri):
        self.conn = await asyncpg.connect(uri, ssl=False)
    async def changePush(self, state, uid):
        await self.conn.execute(
            "UPDATE public.users SET push = $1 WHERE uid = $2",
            state, uid)
        return True
    async def changeState(self, state, uid):
        await self.conn.execute(
            "UPDATE public.users SET state_user = $1 WHERE uid = $2",
            state, uid)
        return True
    async def changeEmail(self, state, uid):
        await self.conn.execute(
            "UPDATE public.users SET email = $1 WHERE uid = $2",
            state, uid)
        return True
    async def setToken(self, state, uid):
        await self.conn.execute(
            "UPDATE public.users SET token = $1 WHERE uid = $2",
            state, uid)
        return True
    async def changeLanguage(self, state, uid):
        await self.conn.execute(
            "UPDATE public.users SET language = $1 WHERE uid = $2",
            state, uid)
        return True
    async def changeNews(self, state, uid):
        await self.conn.execute(
            "UPDATE public.users SET news = $1 WHERE uid = $2",
            state, uid)
        return True

        # try:
        #     await self.conn.execute(
        #         "UPDATE public.users SET push = $1 WHERE uid = $2",
        #         (state, uid))
        #     return True
        # except Exception as e:
        #     print(e)
        #     return False

    async def close(self):
        await self.conn.close()

    async def newUserCheck(self, uid):
        result = await self.query_dict(f'SELECT * FROM public.users WHERE uid = {uid}')
        if not result:
            await self.conn.execute(
                "INSERT INTO public.users(id, uid, state_user, token) VALUES (DEFAULT, $1, 0, 0)",
                (uid))
            return False
        return result[0]