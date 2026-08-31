import functools
import time
from collections.abc import Callable
from typing import Any


def timed(fn: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            elapsed_ms = (time.perf_counter() - start) * 1000
            print(f"[timed] {fn.__name__} took {elapsed_ms:.2f} ms")
    return wrapper