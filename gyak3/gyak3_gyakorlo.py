#GYAKORLO_02:
#1.
#feladat:
while True:
    try:
        x = int(input("Adj meg egy számot: "))
        y = int(input("Adj meg egy számot: "))
        atlag = (x + y) // 2

        if y < 0 or y > 100 or x > 100 or x < 0:
            raise Exception("Nem megfelelő szám!")
        if atlag < 60:
            raise Exception("Megbukott!")
        else:
            print(atlag)
            break

    except Exception as e:
        print(e)

#2.
#feladat:


def avg_in_line(line):
    sum = 0
    db = 0
    line = line.split()
    for n in line:
        if n.isdigit() == True:
            n = int(n)
            if n >= 0:
                sum += n
                db += 1
    if sum == 0:
        print("Nem számolható átlag!")
    else:
        avg = sum // db
        print(avg)


try:
    in_file = open("szamok.txt", "r")
    for line in in_file:
        avg_in_line(line)

    in_file.close()
except FileNotFoundError:
    print('A fájl nem található!')

#3.
#feladat:


def same_letters(line):
    str = ""
    res = ''
    import string
    for ch in line:
        if ch not in string.punctuation:
            str += ch
    str = str.split()
    for word in str:
        if len(word) > 1 and word[0] == word[-1]:
            res += word
            res += " "
    return res


try:
    in_file = open("szoveg.txt", "r")
    out_file = open("out_file2.txt", "w")
    for line in in_file:
        words = same_letters(line)
        if len(words) != 0:
            print(words, file=out_file)
    in_file.close()
    out_file.close()

except FileNotFoundError:
    print('A fájl nem található!')

#GYAKORLO_03:
#1.
#Feladat:
import sys


def str_lists(args):
    list1 = []
    list2 = []
    n = args[0]
    n = int(n)
    str_list = args[1:]
    for str in str_list:
        if len(str) <= n:
            list1.append(str)
        else:
            list2.append(str)
    print(f"list1={list1} list2={list2}")


str_lists(sys.argv[1:])

#2.
#Feladat:
import sys, random


def res_lists(args):
    filename = args[2]
    out_file = open(filename, "w")
    n = args[1]
    n = int(n)
    list1 = []
    list2 = []
    res_list = []
    for i in range(n):
        list1.append(random.randint(0, 10))
        list2.append(random.randint(0, 10))
    for j in range(n):
        res_num = list1[j] * list2[n - 1 - j]
        res_list.append(res_num)
    print(f"Elso lista: {list1} \nMasodik lista: {list2} \nEredmeny: {res_list}", file=out_file)

    out_file.close()


res_lists(sys.argv[0:])

#3.
#feladat:
import sys


def same_ch(args):
    str1 = args[1]
    str2 = args[2]
    list_str1 = []

    for ch in str1:
        list_str1.append(ch)
    for ch in str2:
        if ch not in list_str1:
            return "Hamis"


    if len(str1) == len(str2):
        return "Igaz"

print(same_ch(sys.argv[0:]))
































