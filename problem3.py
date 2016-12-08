
def fibonacci(n = None):
    initial = 0
    previous = 0
    i = 1
    if n == None:
        condition = True
    else:
        condition = False
    while (condition or i <= n) :
        if i == 1 or n == 1:
            current = 1
        else:
            current = initial + previous
        initial = previous
        previous = current
        yield current
        i += 1


for each in fibonacci(4):
    print(each)

