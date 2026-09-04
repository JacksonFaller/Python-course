import asyncio
from collections.abc import Awaitable, Callable, Sequence


async def check_urls(
    urls: Sequence[str],
    check: Callable[[str], Awaitable[int]],
    limit: int = 5,
) -> list[tuple[str, int | None, str | None]]:
    """Return (url, status, error) tuples in input order."""
    # TODO: semaphore + concurrent tasks + failure isolation.
    raise NotImplementedError
