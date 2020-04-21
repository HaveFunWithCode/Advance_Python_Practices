import time
import multiprocessing

start = time.perf_counter()


def do_something(seconds):
    print('start working for {} seconds ....'.format(seconds))
    time.sleep(seconds)
    print('stop working....')


processes = []
for _ in range(10):
    p = multiprocessing.Process(target=do_something, args=[1.5])
    p.start()
    processes.append(p)
for p in processes:
    p.join()
finish = time.perf_counter()

print('total time is ...{}'.format(finish - start))
