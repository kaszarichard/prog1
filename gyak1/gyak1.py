#1.feladat:

n=int(input("Kérek egy számot: "))
while n != 0:
    if n%2==0:
        print("{} egy paros szam!".format(n))
    else:
        print("{} egy paratlan szam!".format(n))

    n = int(input("Kérek egy számot: "))

#2.feladat:

def lnko(a, b):
    if b>a:
        a, b= b, a
    res= 1
    for i in range(2, a+1):
        if a%i==0 and b%i==0:
            res=i
    return res

szamok = input("Kerek ket szamot: ")
a, b = szamok.split()
print("{} és {} lnko-ja: {}".format(a, b,  lnko(int(a), int(b))))

#3.feladat:

first_point = input("Kerem az elso pont kordinatait:")
second_point = input("Kerem a masodik pont kordinatait:")
x1, y1 = first_point.split()
x2, y2 = second_point.split()
x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
import math
dist = math.sqrt((x1 - x2) ** 2 + (y1- y2) ** 2)
#dist=((x1 - x2) ** 2 + (y1- y2) ** 2) **0.5 #gyökvonás
print(dist)

#4.feladat:

def sum_of_digits(n):
    n = str(n)
    sum = 0
#    for ch in n:
#        sum += int(ch)
#    print(sum)

    n = int(n)
    while n != 0:
        sum += n % 10
        n = n // 10
    print(sum)


sum_of_digits(123)

#5.feladat:

def list_of_words(words):
    word_list = words.split(",")
    res =[]
#    print(word_list)
    for word in word_list:
        word = word.strip()    #sztring körül lévő szóközöket eltávolítja
        if word not in res:
            res.append(word)
    return sorted(res) #rendezi a listában szereplő értékeket, van egy paramétere, ha ez True akkor megfordítja a sorrendet(paraméter neve: reverse)


print(list_of_words('alma, kecske, banan, dio, alma, fa, banan, korte'))

#6.feladat:

def first_three_letters(word):
    if len(word) < 3:
        return word
    return word[:3] #a szó első három karaktere

print(first_three_letters('fa'))