from cProfile import Profile
from pstats import SortKey, Stats

from sieveOfEratosthenes import sieveOfEratosthenes

with Profile() as profile:
    sieveOfEratosthenes(1000000)
    (
         Stats(profile)
         .strip_dirs()
         .sort_stats(SortKey.CUMULATIVE)
         .print_stats(300)
    )