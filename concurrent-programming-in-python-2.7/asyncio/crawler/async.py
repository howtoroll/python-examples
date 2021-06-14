# requires Python 3.7+
import sys
import time
import requests
import asyncio


start_time = time.time()
loop = asyncio.get_event_loop()


async def send_req(url):
    t = time.time()
    print("Send a request at", t-start_time, "seconds.")

    res = await loop.run_in_executor(None, requests.get, url)

    t = time.time()
    print("Receive a response at", t-start_time, "seconds.")


def main():
    url = 'https://www.google.com.tw/'
    tasks = []
    for i in range(10):
        task = loop.create_task(send_req(url))
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))


if __name__ == "__main__":
    sys.exit(main())
