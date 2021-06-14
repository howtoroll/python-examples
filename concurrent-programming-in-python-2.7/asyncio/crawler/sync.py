# requires Python 3.7+
import sys
import time
import requests


start_time = time.time()


def send_req(url):
    t = time.time()
    print("Send a request at", t-start_time, "seconds.")

    res = requests.get(url)

    t = time.time()
    print("Receive a response at", t-start_time, "seconds.")


def main():
    url = 'https://www.google.com.tw/'
    for i in range(10):
        send_req(url)


if __name__ == "__main__":
    sys.exit(main())
