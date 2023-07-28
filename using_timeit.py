import timeit

from sieveOfEratosthenes import sieveOfEratosthenes

iters = 100
total_time = timeit.timeit(stmt='sieveOfEratosthenes(1000000)', number=iters, globals=globals())
print(total_time/iters)