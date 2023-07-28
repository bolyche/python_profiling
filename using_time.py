import time
import functools

from sieveOfEratosthenes import sieveOfEratosthenes

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tic = time.perf_counter(), time.process_time()
        value = func(*args, **kwargs)
        toc = time.perf_counter(), time.process_time()
        elapsed_time_real = toc[0] - tic[0]
        elapsed_time_cpu =  toc[1] - tic[1]
        print(f"------------timer------------\nCall: {func.__name__}\nReal time: {elapsed_time_real:0.4f} secs\nCPU time: {elapsed_time_cpu:0.4f} secs")
        return value
    return wrapper

example = timer(sieveOfEratosthenes)
example(1000000)