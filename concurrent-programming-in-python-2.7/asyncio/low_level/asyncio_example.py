# requires Python 3.7+
import sys
import asyncio


loop = asyncio.get_event_loop()


async def example_01():
    print("Start example_01 coroutine.")
    await asyncio.sleep(1)
    print("Finish example_01 coroutine.")


async def example_02():
    print("Start example_02 coroutine.")
    await asyncio.sleep(1)
    print("Finish example_02 coroutine.")


def main():
    #loop.run_until_complete(example_01())

    #tasks = [
    #    asyncio.ensure_future(example_01()),
    #    asyncio.ensure_future(example_02()),
    #]
    #loop.run_until_complete(asyncio.wait(tasks))

    tasks = [
        loop.create_task(example_01()),
        loop.create_task(example_02())
    ]
    loop.run_until_complete(asyncio.wait(tasks))


if __name__ == "__main__":
    sys.exit(main())
