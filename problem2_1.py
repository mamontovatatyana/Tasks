from time import sleep, time
from random import randint

def timemeasure(t_max):
    def decorator(fn):
        def wrapper(*x):
            a = time()
            X = fn(*x)
            b = time()
            if t_max < (b - a):
                return print('Time delay %d',b-a)
            else:
                return X
        return wrapper
    return decorator


@timemeasure(5)
def f(message):
    delay = randint(1,10)
    sleep(delay)
    return print(message)

f('Hello')