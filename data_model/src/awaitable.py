
class Awaitable:

    def __await__(self):
        async def a():
            return 'hi async world'

        return a().__await__()
