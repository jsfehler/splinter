import time

import pytest

from splinter.retry import _retry


def true_in_5_seconds(start: int) -> bool:
    now = time.time()

    if now >= start + 5:
        return True
    return False


def always_false() -> bool:
    return False


def raises_exception() -> None:
    raise Exception("ded")


def test_retry_until_timeout_truthy_found():
    """
    Given a function that will return a truthy value after an amount of time
    When I set a timeout for _retry()
    Then it will retry a function for the set amount of time
    """
    start_time = time.time()

    assert _retry(true_in_5_seconds, [start_time], timeout=5)

    assert time.time() >= start_time + 5


def test_retry_until_timeout_falsey_found():
    """
    Given a function that will return a falsey value no matter what
    When I set a timeout for _retry()
    Then it will retry a function for the set amount of time
    """
    start_time = time.time()

    result = _retry(always_false, timeout=5)

    assert time.time() >= start_time + 5

    assert result is False


def test_retry_no_timeout():
    """
    Given a function that will return a truthy value after an amount of time
    When there is no timeout set
    Then _retry() will return False
    """
    start_time = time.time()

    assert _retry(true_in_5_seconds, [start_time]) is False


def test_retry_raises_exception():
    """
    Given a function that will raise an Exception
    When I set a timeout for _retry()
    Then the timeout is not respected
    And an Exception is raised
    """
    with pytest.raises(Exception) as e:
        _retry(raises_exception, timeout=5)

    assert str(e.value) == "ded"
