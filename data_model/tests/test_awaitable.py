from pytest import mark

from src.awaitable import Awaitable


@mark.asyncio
async def test_awaitable():
    awaitable = Awaitable()
    assert await awaitable == 'hi async world'
