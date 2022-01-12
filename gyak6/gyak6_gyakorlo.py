import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

def arfolyamok():
    res = np.zeros(20)
    in_file = open("arfolyam.txt","r")
    i = 0
    for line in in_file:
        nums = line.split()
        for n in nums:
            res[i] = n
            i += 1
    return res

def convert_to_grayscale(image):
    return image[:,:,0] * 0.2989 + image[:,:,1] * 0.5870 + image[:,:,2] * 0.1140

def bin_img(image):
    avg = np.mean(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i,j]>avg:
                image[i,j] = 255
            else:
                image[i, j] = 0
    return image

def reverse_intens(image):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i, j]=255-image[i, j]
    return image


# 1.feladat:
# x = np.arange(1,11)
# res = arfolyamok()
# penznem1=res[:10]
# penznem2=res[10:20]
# plt.plot(x, penznem1,"b", label= "pénznem1")
# plt.plot(x, penznem2,"orange", label = "pénznem2")
# plt.xlabel("napok")
# plt.ylabel("HUF")
# plt.title("Árfolyamváltozás")
# plt.legend()
# plt.show()

# 2.feladat:
# image=img.imread("flowers.jpg")
# gray =convert_to_grayscale(image)
# bin_image=bin_img(gray)
# plt.imshow(bin_image, cmap="gray")
# plt.show()

# 3.feladat:
image=img.imread("flowers.jpg")
gray =convert_to_grayscale(image)
reversed_img=reverse_intens(gray)
plt.imshow(reversed_img,cmap="gray")
plt.show()
