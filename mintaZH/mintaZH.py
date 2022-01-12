#MintaZH:
#1.feladat:
mgh = "aeiou"

def insert_num(word):
    n = 1
    res = ""
    for ch in word:
        if ch in mgh:
            res += ch +str(n)
        else:
            res += ch
        n+=1

while True:
    word = input("Kerek egy szot: ")
    if word == "end":
        break
    # n = 1
    # res = ""
    # for ch in word:
    #     if ch in mgh:
    #         res += ch +str(n)
    #     else:
    #         res += ch
    #     n+=1
    print(insert_num(word))

#2.feladat:
import sys

n = int(sys.argv[1])
out_filename = sys.argv[2]

def remove_punctuations(line):
    import string
    new_line = ''
    for ch in line:
        if ch not in string.punctuation:
            new_line += ch
    return new_line
out_file = open(out_filename, 'w')
with open('input.txt','r') as in_file:
    for line in in_file:
        line = remove_punctuations(line)
        words = line.split()
        for word in words:
            if len(word) == n:
                print(word, file=out_file)

out_file.close()

#3.feladat:
import numpy as np

vec = np.random.randint(1, 100, 10)
avg = np.average(vec)
dist = np.abs(vec - avg)
dist[dist < 10] = 0

print(vec)
print(avg)
print(dist)

# 4.feladat:
# import numpy as np

rows = int(input("Kerem a sorok szamat: "))
columns = int(input("Kerem az oszlopok szamat: "))

low = int(input("Kerem az intervallum also korlatjat: "))
high = int(input("Kerem az intervallum felso korlatjat: "))

n = int(input("Kerek egy szamot: "))

mtx = np.random.randint(low, high,(rows, columns))

def sum_of_num(number):
    number = str(number)
    sum = 0
    for ch in number:
        sum += int(ch)
    return sum

res = []

print(mtx)

for j in range(mtx.shape[1]):
    count = 0
    for i in range(mtx.shape[0]):
        sum = sum_of_num(mtx[i, j])
        if sum > n:
            count +=1
    if count >= mtx.shape[0] / 2:
        res.append(j + 1)
print(res)

#5.feladat:
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

def fv1(x):
    return (3 * x + 2) ** 2

def fv2(x):
    return (3 * x -2) / x

x = np.arange(-25, 26)
y1 = fv1(x)
y2 = fv2(x)

fig, ax = plt.subplots(1, 2)
ax[0].plot(x, y1, 'g')
ax[1].plot(x, y2, 'r')
ax[0].set_title("Elso fuggveny")
ax[1].set_title("Masodik fuggveny")
plt.show()



