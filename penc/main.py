import os
import matplotlib.pyplot as plt
from skimage.color.colorconv import rgb2gray
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops
from skimage import morphology

directory = os.listdir(path='img')
amount = 0

for filename in directory:
    img = plt.imread('./img/'+filename)

    grayscale = rgb2gray(img)
    thresh = threshold_otsu(grayscale)
    binary = grayscale < thresh
    erosion = morphology.binary_erosion(binary)
    dilation = morphology.binary_dilation(erosion)
    labeled = label(dilation)
    labeled = labeled[50:-50, 50:-50]
    regions = regionprops(labeled)


    cnt = 0
    for region in regions:
        # elongation of the figure
        if region.eccentricity > 0.99 and region.equivalent_diameter > 170:
            cnt += 1

    amount += cnt
    print(filename, cnt)

print(amount)