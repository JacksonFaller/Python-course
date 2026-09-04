import asyncio
from collections.abc import Awaitable, Callable, Sequence


async def check_urls(
    urls: Sequence[str],
    check: Callable[[str], Awaitable[int]],
    limit: int = 5,
) -> list[tuple[str, int | None, str | None]]:
    semaphore = asyncio.Semaphore(limit)

    async def run(url: str) -> tuple[str, int | None, str | None]:
        async with semaphore:
            try:
                return url, await check(url), None
            except Exception as exc:
                return url, None, str(exc)

    return await asyncio.gather(*(run(url) for url in urls))
