import sys
import time
import multiprocessing as mp


def simpleUse():
    def job():
        for i in range(5):
            print "Child process: " + str(i)
            time.sleep(10)

    p = mp.Process(target=job)
    p.start()

    for i in range(5):
        print "Main process: " + str(i)
        time.sleep(1)

    p.join()
    print "simpleUse done"


def simpleUseWithParam():
    def job(num):
        print "New process: " + str(num)
        time.sleep(10)
        print "New process: " + str(num) + " done"

    processes = []
    for i in range(3):
        processes.append(mp.Process(target=job, args=(i,)))
        processes[i].start()

    for i in range(5):
        print "Main process: " + str(i)
        time.sleep(1)

    for i in range(3):
        processes[i].join()
    print "simpleUseWithParam done"


def main():
    # simpleUse()
    simpleUseWithParam()


if __name__ == "__main__":
    sys.exit(main())
