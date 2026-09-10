import threading
import time

import pytest

from .solution import bounded_map


def test_preserves_order_and_uses_multiple_threads() -> None:
    thread_ids: set[int] = set()
    lock = threading.Lock()

    def work(value: int) -> int:
        with lock:
            thread_ids.add(threading.get_ident())
        time.sleep(0.01)
        return value * value

    assert bounded_map(work, range(6), max_workers=3) == [0, 1, 4, 9, 16, 25]
    assert len(thread_ids) > 1


def test_validates_worker_count_and_propagates_exceptions() -> None:
    with pytest.raises(ValueError, match="positive"):
        bounded_map(str, [1], max_workers=0)

    def fail(_: int) -> int:
        raise RuntimeError("task failed")

    with pytest.raises(RuntimeError, match="task failed"):
        bounded_map(fail, [1], max_workers=1)
