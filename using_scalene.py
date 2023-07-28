from scalene import scalene_profiler

from sieveOfEratosthenes import sieveOfEratosthenes

scalene_profiler.start()
sieveOfEratosthenes(1000000)
scalene_profiler.stop()

# run using `scalene using_scalene.py`