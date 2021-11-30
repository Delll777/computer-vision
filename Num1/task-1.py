import numpy as np
from collections import Counter

for i in range(1, 7):
    with open(f'C:/#AllNeeds/Study/Comp-vision/Num1/figure{i}.txt') as file:
        size_mm = float(file.readline())
        file.readline()
        image = np.loadtxt(file)
        arr = np.nonzero(image[:])
        counter = Counter(arr[0])
        if counter:
            pixels = max([elem for elem in counter.values()])
            print(f'{i}: {size_mm / pixels}')
        else:
            print(f'{i}: no image')