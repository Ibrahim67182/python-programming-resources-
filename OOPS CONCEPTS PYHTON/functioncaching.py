from functools import lru_cache
import time

@lru_cache(maxsize=None)
def square(x):
   
    time.sleep(4)
    print(f"square {x} is : {x*x}")


# firstly they are not into memory so they take 4 sec each to execute

square(2)
square(5)
square(7)


# they are already in cache now they execute directly and faster

square(2)
square(5)
square(7)

#this is a new value it will be executed after 4 secs
square(9)

