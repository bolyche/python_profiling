from pyinstrument import Profiler

from sieveOfEratosthenes import sieveOfEratosthenes

profiler = Profiler()
profiler.start()
sieveOfEratosthenes(1000000)
profiler.stop()
profiler.print()