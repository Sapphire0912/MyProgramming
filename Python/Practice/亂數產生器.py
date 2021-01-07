import numpy as np


def randoms(numbers=1, tuples=1, _min=0, _max=100):
    x = np.zeros((tuples, numbers))

    for i in range(tuples):
        j = 0
        while True:
            if j == numbers:
                break
            
            r = np.random.randint(_min, _max + 1)
            if r in x[i]:
                continue
            else:
                x[i, j] = r
                j += 1
    x = np.sort(x)
    return x


print(randoms(5, 10, 1, 39))
