import asyncio

import pytest

from exercises.module08.checker import check_urls


@pytest.mark.asyncio
async def test_checks_are_concurrent_and_order_is_preserved():
    async def fake_check(url: str) -> int:
        await asyncio.sleep(0.01 if url == "slow" else 0)
        return {"a": 200, "slow": 201, "c": 204}[url]

    result = await check_urls(["a", "slow", "c"], fake_check, limit=2)
    assert result == [("a", 200, None), ("slow", 201, None), ("c", 204, None)]


@pytest.mark.asyncio
async def test_failures_are_isolated():
    async def fake_check(url: str) -> int:
        if url == "bad":
            raise TimeoutError("timed out")
        return 200

    result = await check_urls(["ok", "bad"], fake_check)
    assert result == [("ok", 200, None), ("bad", None, "timed out")]


@pytest.mark.asyncio
async def test_concurrency_is_limited():
    current = 0
    maximum = 0

    async def fake_check(url: str) -> int:
        nonlocal current, maximum
        current += 1
        maximum = max(maximum, current)
        await asyncio.sleep(0)
        current -= 1
        return 200

    await check_urls([str(i) for i in range(20)], fake_check, limit=3)
    assert maximum <= 3
