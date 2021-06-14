from gevent import monkey; monkey.patch_all()

import sys
import gevent
from gevent.queue import Queue
import socket


def simpleUseV1():
    def test1():
        print 12
        gevent.sleep(0)
        print 34

    def test2():
        print 56
        gevent.sleep(0)
        print 78

    gevent.joinall([
        gevent.spawn(test1),
        gevent.spawn(test2),
    ])


def simpleUseV2():
    urls = ['www.baidu.com', 'www.gevent.org', 'www.python.org']
    jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
    gevent.joinall(jobs, timeout=5)

    print [job.value for job in jobs]


def simpleUseMonkeyPatching():
    # use monkey.patch_socket() or monkey.patch_all()
    urls = ['www.baidu.com', 'www.gevent.org', 'www.python.org']
    jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
    gevent.joinall(jobs, timeout=5)

    print [job.value for job in jobs]


def simpleUseSpawnState():
    def win():
        return 'You win!'

    def fail():
        raise Exception('You failed!')

    winner = gevent.spawn(win)
    loser = gevent.spawn(fail)

    print winner.started  # True
    print loser.started   # True

    try:
        gevent.joinall([winner, loser])
    except Exception:
        print 'This will never be reached'

    print winner.ready()  # True
    print loser.ready()   # True

    print winner.value  # 'You win!'
    print loser.value   # None

    print winner.successful()  # True
    print loser.successful()   # False

    print loser.exception


def simpleUseQueue():
    products = Queue()

    def consumer(name):
        while not products.empty():
            print '%s got product %s' % (name, products.get())
            gevent.sleep(0)
        print '%s Quit' % (name)

    def producer():
        for i in xrange(1, 10):
            products.put(i)

    gevent.joinall([
        gevent.spawn(producer),
        gevent.spawn(consumer, 'steve'),
        gevent.spawn(consumer, 'john'),
        gevent.spawn(consumer, 'nancy'),
    ])


def main():
    # simpleUseV1()
    # simpleUseV2()
    # simpleUseMonkeyPatching()
    # simpleUseSpawnState()
    simpleUseQueue()


if __name__ == "__main__":
    sys.exit(main())
