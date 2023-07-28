from line_profiler import LineProfiler

from sieveOfEratosthenes import sieveOfEratosthenes

lp = LineProfiler()
sieve_timing = lp(sieveOfEratosthenes)
sieve_timing(1000000)

lp.print_stats()