#1.feladat:
import numpy as np
def reverse_array(a):
    b = np.array(a[a.size-1])
    for i in range(a.size - 2, -1, -1):
        b = np.append(b, a[i])
    return b

a = np.arange(10, 50)
print(a)
b = reverse_array(a)
print(b)

#2.feladat:
import numpy as np

def min_max(a):

    min = a[0]
    max = a[0]
    min_idx = 0
    max_idx = 0

    for i in range(1, len(a)):
        if a[i] > max:
            max = a[i]
            max_idx = i
        if a[i]<min:
            min = a[i]
            min_idx = i
    return min, max, min_idx, max_idx

c=np.random.randint(0, 50, 30)
print(c)
min_max_values = c[(c == c.min()) or (c == c.max())]
min_max_includes = np.where((c == c.min()) or (c == c.max()))
print(min_max_includes)
print(min_max_includes[0][0])

#3.feladat:
import numpy as np

d = np.random.randint(0, 50, 30)
print(d, d.max())
d[d == d.max()] = -1
print((d))

#4.feladat:
import numpy as np
def sort_vector(a):
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a

e = np.random.randint(0, 10, 10)
print(e)
e = np.sort(e, kind='quicksort')
print(e)

#5.feladat:
import numpy as np

f = np.random.randint(0, 10, 50)
print(f)
f[(f >= 3) & (f <= 8)] *= -1
print(f)

#6.feladat:
import numpy as np
def find_min_dist(a, n):
    min_dist = abs(a[0] - n)
    min_idx = 0

    for i in range(1, len(a)):
        if abs(a[i] - n)<min_dist:
            min_idx = i
            min_dist = abs(a[i] - n)
    return min_idx


g = np.random.randint(0, 50, 10)
n = int(input("Kerek egy szamot: "))
dist = np.abs(g - n)
indices = np.where(dist == dist.min())
values = g[dist == dist.min()]
print((values, indices))

#7.feladat:
import  numpy as np

h = np.random.randint(-50, 50, 100)
pos = h[h > 0].size
neg = h[h < 0].size
zeros = h[h == 0].size
print(f"Pozitivak: {pos}\nNegativak: {neg}\nNullak: {zeros}")



























