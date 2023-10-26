"""
The main purpose of this module is implementing separate
processes interaction interface.

Obviously once the Python3.12 works in production
this one could be replaced with threading module instead.
"""

import asyncio
from multiprocessing import Process
from typing import Any, Callable, Coroutine

from loguru import logger

from .errors import ProcessError

__all__ = ("_ProcessBlock",)


_ProcessBlock = tuple[Callable, str, str]


# NOTE: This place is definitelly should be replaced
#       with something more sophisticated.
_PROCESSES: dict[str, Process] = {}


def _build_key(namespace: str, key: Any) -> str:
    """Builds the unique key base on the namespace."""

    return f"{namespace}_{str(key)}"


def get(namespace: str, key: Any) -> Process:
    """Get the process from the register if exist."""

    _key = _build_key(namespace, key)
    try:
        return _PROCESSES[_key]
    except KeyError:
        raise ProcessError(message=f"Process {_key} does not exist.")


def kill(namespace: str, key: Any) -> None:
    """Kill the process base on the namespace and key."""

    process: Process = get(namespace, key)
    process.terminate()
    _key = _build_key(namespace, key)
    del _PROCESSES[_key]
    logger.success(f"The process {_key} is terminated")

    # NOTE: Only for threads
    # raise NotImplementedError


def _run_coro(coro_func: Callable[..., Coroutine], *args, **kwargs) -> None:
    """Run the coroutine in the event loop.
    Used as a helper function for the run function.
    """

    asyncio.run(coro_func(*args, **kwargs))


def run(
    namespace: str,
    key: Any,
    callback: Callable | Callable[..., Coroutine],
    **kwargs: Any,
) -> Process:
    """Run the process and register it for future management.
    If the callback is a coroutine, it will be run in a event loop.
    """

    if (_key := _build_key(namespace, key)) in _PROCESSES.keys():
        raise ProcessError(message=f"Process {_key} already exist")

    task: Process = (
        Process(target=_run_coro, args=(callback,), kwargs=kwargs, daemon=True)
        if asyncio.iscoroutinefunction(callback)
        else Process(target=callback, kwargs=kwargs, daemon=True)
    )
    task.start()

    _PROCESSES[_key] = task

    logger.debug(f"Background process is running: {_key}")

    return task
