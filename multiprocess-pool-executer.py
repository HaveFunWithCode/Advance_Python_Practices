import os
import time
import concurrent.futures


def do_something(seconds):
    print('in process_id :{}---->start working for {} seconds  '.format( os.getpid(), seconds))
    time.sleep(seconds)
    return 'stop working....{}'.format(seconds)


def get_result_based_on_process_finished_order():
    """  get result based on process finished order """

    with concurrent.futures.ProcessPoolExecutor() as executer:
        secs = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        results = [executer.submit(do_something, sec) for sec in secs]
        for f in concurrent.futures.as_completed(results):
            print(f.result())


def get_result_based_on_process_input_order():
    """  get result based on process finished order"""

    with concurrent.futures.ProcessPoolExecutor() as executer:
        secs = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        results = executer.map(do_something, secs)
        for res in results:
            print(res)


if __name__ == "__main__":
    print("--------------------get result based on process input order :------------------------------")
    start = time.perf_counter()
    get_result_based_on_process_input_order()
    finish = time.perf_counter()
    print('total time is ...{}'.format(finish - start))

    print("--------------------get result based on process finished order :------------------------------")
    start = time.perf_counter()
    get_result_based_on_process_finished_order()
    finish = time.perf_counter()
    print('total time is ...{}'.format(finish - start))
