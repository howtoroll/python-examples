import sys
import time
import threading
import Queue as queue  # p27


def simpleUse():
    def job():
        for i in range(5):
            print "Child thread: " + str(i)
            time.sleep(1)

    t = threading.Thread(target=job)
    t.start()

    for i in range(5):
        print "Main thread: " + str(i)
        time.sleep(1)

    t.join()
    print "simpleUse done"


def simpleUseWithParam():
    def job(num):
        print "New thread: " + str(num)
        time.sleep(10)
        print "New thread: " + str(num) + " done"

    threads = []
    for i in range(5):
        threads.append(threading.Thread(target=job, args=(i,)))
        threads[i].start()

    for i in range(5):
        print "Main thread: " + str(i)
        time.sleep(1)

    for i in range(5):
        threads[i].join()
    print "simpleUseWithParam done"


def simpleUseWithOOP():
    class MyThread(threading.Thread):
        def __init__(self, num):
            threading.Thread.__init__(self)
            self.num = num

        def run(self):
            print "New thread: " + str(self.num)
            time.sleep(10)
            print "New thread: " + str(self.num) + " done"

    threads = []
    for i in range(5):
        threads.append(MyThread(i))
        threads[i].start()

    for i in range(5):
        print "Main thread: " + str(i)
        time.sleep(1)

    for i in range(5):
        threads[i].join()
    print "simpleUseWithOOP done"


def simpleUseWithQueue():
    class Worker(threading.Thread):
        def __init__(self, queue, num):
            threading.Thread.__init__(self)
            self.queue = queue
            self.num = num

        def run(self):
            while self.queue.qsize() > 0:
                msg = self.queue.get()
                print "Worker: " + str(self.num) + " Msg: " + msg
                time.sleep(1)

    my_queue = queue.Queue()
    for i in range(10):
        my_queue.put("Data %d" % i)

    my_worker1 = Worker(my_queue, 1)
    my_worker2 = Worker(my_queue, 2)

    my_worker1.start()
    my_worker2.start()

    for i in range(5):
        print "Main thread: " + str(i)
        time.sleep(1)

    my_worker1.join()
    my_worker2.join()
    print "simpleUseWithQueue done"


def simpleUseWithQueueAndLock():
    class Worker(threading.Thread):
        def __init__(self, queue, num, lock):
            threading.Thread.__init__(self)
            self.queue = queue
            self.num = num
            self.lock = lock

        def run(self):
            while self.queue.qsize() > 0:
                # might not FIFO due to lock
                msg = self.queue.get()

                self.lock.acquire()
                print "Lock acquired by Worker: " + str(self.num)

                print "Worker: " + str(self.num) + " Msg: " + msg
                time.sleep(1)

                print "Lock released by Worker: " + str(self.num)
                self.lock.release()

    my_queue = queue.Queue()
    for i in range(10):
        my_queue.put("Data %d" % i)

    lock = threading.Lock()

    my_worker1 = Worker(my_queue, 1, lock)
    my_worker2 = Worker(my_queue, 2, lock)

    my_worker1.start()
    my_worker2.start()

    my_worker1.join()
    my_worker2.join()
    print "simpleUseWithQueueAndLock done"


def main():
    # simpleUse()
    # simpleUseWithParam()
    # simpleUseWithOOP()
    # simpleUseWithQueue()
    simpleUseWithQueueAndLock()


if __name__ == "__main__":
    sys.exit(main())
