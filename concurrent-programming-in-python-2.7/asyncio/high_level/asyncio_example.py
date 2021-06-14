# requires Python 3.7+
import sys
import time
import datetime
import asyncio


async def coroutines_01():
    print('Hello 01 ...')
    await asyncio.sleep(3)
    print('... World!')


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def coroutines_02():
    print(f"started at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f"finished at {time.strftime('%X')}")


async def coroutines_03():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")


async def nested():
    print(42)


async def awaitables_01():
    # coroutines

    # nothing happens if we just call "nested()"
    # RuntimeWarning
    #nested()

    await nested()


async def awaitables_02():
    # tasks

    task = asyncio.create_task(nested())
    await task


async def awaitables_03():
    # futures

    #await function_that_returns_a_future_object()

    # this is also valid:
    #await asyncio.gather(
    #    function_that_returns_a_future_object(),
    #    some_python_coroutine()
    #)
    pass


async def sleeping_01():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")


async def gather_01():
    # schedule three calls *concurrently*:
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )


async def eternity():
    # sleep for one hour
    await asyncio.sleep(3600)
    print('yay!')


async def timeout_01():
    # wait for at most 3 second
    try:
        await asyncio.wait_for(eternity(), timeout=3.0)
    except asyncio.TimeoutError:
        print('timeout!')


async def cancel_me():
    print('cancel_me(): before sleep')

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')


async def cancel_01():
    # create a "cancel_me" Task
    task = asyncio.create_task(cancel_me())

    # wait for 1 second
    await asyncio.sleep(1)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")


def main():
    if sys.version_info[0] < 3:
        return

    """
        Coroutines
    """
    #asyncio.run(coroutines_01())

    # simply calling a coroutine will not schedule it to be executed
    # RuntimeWarning
    #coroutines_01()

    #asyncio.run(coroutines_02())

    #asyncio.run(coroutines_03())

    """
        Awaitables
    """
    #asyncio.run(awaitables_01())

    #asyncio.run(awaitables_02())

    #asyncio.run(awaitables_03())

    """
        Sleeping
    """
    #asyncio.run(sleeping_01())

    """
        Running Tasks Concurrently (gather)
    """
    #asyncio.run(gather_01())

    """
        Timeouts
    """
    #asyncio.run(timeout_01())

    """
        Task Object (cancel)
    """
    asyncio.run(cancel_01())


if __name__ == "__main__":
    sys.exit(main())
