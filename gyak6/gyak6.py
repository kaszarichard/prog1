import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.power(np.e,-x))

def sigmoid_derivate(x):
    return sigmoid(x) * (1 - sigmoid(x))

#1.feladat
x = np.arange(-3,3,0.01)
y = sigmoid(x) #az egesz vektor atadhato a fv-nek
dy = sigmoid_derivate(x)

plt.plot(x,y,'g-',label="sigmoid")
plt.plot(x,dy,'r-',label="sigmoid derivate")
plt.xlabel("X értékek") #x tengely cime
plt.ylabel('Y értékek') #y tengely cime
plt.title("Sigmoid függvény") #az egesz abra cime
plt.legend() #jelmagyarazat bekapcsolasa
plt.show()

#2.feladat
def histogram(mtx):
    h = np.zeros(20) # lehetseges elemek
    for i in range(20):
        h[i] = np.sum(mtx == i) # az i-edik elem elofordulasainak szama a matrixban
    return h

mtx = np.random.randint(0,20,(100,100)) # random matrix
h = histogram(mtx)

plt.bar(range(20),h) #oszlopdiagram abrazolas
plt.show()

#3.feladat
# import matplotlib.pyplot as plt
import matplotlib.image as img
# import numpy as np

def convert_to_grayscale(image):
    gray = np.uint8(0.2989 * image[:,:,0] + 0.5870 * image[:,:,1] + 0.1140 * image[:,:,2])
    return gray

image = img.imread('flowers.jpg')
fig, ax = plt.subplots(1,3)
ax[0].imshow(image[:,:,0], cmap='gray')
ax[0].set_xlabel('Red')
ax[1].imshow(image[:,:,1], cmap='gray')
ax[1].set_xlabel('Green')
ax[2].imshow(image[:,:,2], cmap='gray')
ax[2].set_xlabel('Blue')
fig.suptitle('RGB')
plt.show()
image_gray = convert_to_grayscale(image)
plt.imshow(image_gray, cmap='gray')
plt.show()

#4.feladat
# import matplotlib.pyplot as plt
# import matplotlib.image as img
# import numpy as np

def rgb2gray(image):
    gray = np.uint8(0.2989 * image[:,:,0] + 0.5870 * image[:,:,1] + 0.1140 * image[:,:,2])
    return gray

def sorok_torol(image):
    avg_kep = np.mean(image) # az egesz kep ertekeinek atlaga
    row_avg = image.mean(axis = 1) # sorok ertekeinek atlaga
    for i in range(image.shape[0]): # minden soron vegighaladva
        if row_avg[i] > avg_kep: # ha nagyobb az adott sor atlaga
            image[i,:] = np.zeros(image.shape[1]) # csere csak 0 vektorra

image = img.imread('flowers.jpg')
gray = rgb2gray(image)


plt.subplot(1,2,1)
plt.imshow(gray,cmap="gray")
plt.subplot(1,2,2)
sorok_torol(gray)
plt.imshow(gray,cmap="gray")
plt.show()

#5.feladat
# import matplotlib.pyplot as plt
# import matplotlib.image as img
# import numpy as np

def convert_to_grayscale(image):
    gray = np.uint8(0.2989 * image[:,:,0] + 0.5870 * image[:,:,1] + 0.1140 * image[:,:,2])
    return gray

def mean_filter(image,mask_size):
    res_image = np.zeros_like(image)
    for i in range(mask_size,image.shape[0] - mask_size):
        for j in range(mask_size, image.shape[1] - mask_size):
            res_image[i,j] = np.mean(image[i - mask_size: i + mask_size, j - mask_size: j + mask_size])

    return res_image

image = img.imread('flowers.jpg')
gray = rgb2gray(image)

image = img.imread('flowers.jpg')
image = convert_to_grayscale(image)
new_im = mean_filter(image, 15)
fig, ax = plt.subplots(1,2)
ax[0].imshow(image, cmap='gray')
ax[1].imshow(new_im, cmap='gray')
plt.show()