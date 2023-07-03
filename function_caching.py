# function caching

from functools import lru_cache
import time

@lru_cache #(maxsize=None) # maxsize is no.of values to be stored . by default is None
def timetaking(x):
    time.sleep(3)
    return (x*2)

print(timetaking(23))
print(timetaking(2))
print(timetaking(3))
print(timetaking(22))
print(timetaking(36))
# function won't take time for below values as they are repeated and their RETURN value is stored in lru_cache
print(timetaking(2))
print(timetaking(23))
print(timetaking(3))
