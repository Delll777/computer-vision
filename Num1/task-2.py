import numpy as np

def func(path):
    with open(path) as file:
        file.readline()
        file.readline()
        image = np.loadtxt(file)
        indexes = np.nonzero(image[:])
    return indexes

img1 = 'C:/#AllNeeds/Study/Comp-vision/Num1/img1.txt'
img2 = 'C:/#AllNeeds/Study/Comp-vision/Num1/img2.txt'

indexes_img1 = func(img1)
indexes_img2 = func(img2)

print((indexes_img1[0] - indexes_img2[0])[0], (indexes_img1[1] - indexes_img2[1])[0])