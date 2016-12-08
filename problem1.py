def quicksort(a):
    if len(a) == 0:
        return []
    else:
        mid = a[0]
        x = quicksort([each for each in a[1:] if each < mid])
        y = quicksort([each for each in a[1:] if each > mid])
        equal = [each for each in a if each == mid]
        return x + equal +y

print(quicksort([5,2,5,1,3,9,1,7,4]))