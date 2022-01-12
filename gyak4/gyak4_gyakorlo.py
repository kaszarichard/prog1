import numpy as np

def write_to_file(file_name,d):
    d = np.sort(d)
    out_file=open(file_name,"w")
    next_item = 1
    max_freq = 0
    most_common = 1
    freq_in_array = 1
    for i in range(len(d)):

        if next_item==d[i]:
            freq_in_array += 1

            if freq_in_array>max_freq:
                max_freq=freq_in_array
                most_common = next_item
        else:
            next_item+=1
            freq_in_array = 1
    print(f"Vektor: {d}\nA legtobbet szeeplo szam: {most_common}\nElofordulasok szama: {max_freq}", file=out_file)

def random_array(a, b, c):
    e = np.random.randint(a, b, c)
    avg = np.average(e)
    items = []
    place_of_items = np.array([], int)
    for i in range(len(e)):
        if e[i]<avg and e[i]%2==0:
            items.append(e[i])
            place_of_items = np.append(place_of_items, i)
    print(f"Vektor: {e}\nElemek: {items}\nHelyeik: {place_of_items} ")



# 1.feladat
# a = np.random.randint(0,20, 10)
# avg = np.average(a)
# res = np.array([])
#
# for i in range(a.size):
#     dis = abs(a[i]-avg)
#     res=np.append(res, dis)
# print(res)

# 2.feladat:
# while True:
#     try:
#             b = np.random.randint(1, 90, 5)
#             n = int(input("Kerek egy szamot: "))
#             if n not in b:
#                 raise Exception("Nem talált!")
#             else:
#                 print("Találat")
#                 break
#     except Exception as e:
#         print(e)

#3.feladat:
# c = np.arange(1, 300, 3)
# counter = 0
# for i in range(len(c)-1):
#
#     if c[i]%4==0:
#         c[i]=-4
#         counter += 1
# print(counter)

#4.feladat:
# file_name=input("Fajlnev: ")
# d = np.random.randint(1, 10, 50)
# write_to_file(file_name,d)

#5.feladat:
a, b, c = 5, 50, 10
random_array(a, b, c)
