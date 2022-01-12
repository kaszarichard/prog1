import numpy as np

# a = np.matrix([[1,2],[3,4],[5,6]])
# print(a)

# b = np.random.randint(1,10,(3,4))    #3-a sor, 4 az oszlopszáám
# print(b)

# c = np.ones((2,2))  #egyesekkel feltöltött
# print(c)

# d = np.zeros((3,5)) #0-val tölti fel
# print(d)

# b = np.random.randint(1,10,(3,4))
# print(b)

# print((b.shape))    #tárolja a sorok és az oszlopok számát
# print(b.shape[0])   #sor száma
# print(b.shape[1])   #oszlop száma bejárásnál

# for i in range(b.shape[0]): #sorfolytonos bejárás
#     for j in range(b.shape[1]):
#         print(b[i,j], end=" ")
#     print()
# for j in range(b.shape[1]): #oszlopfolytonos bejárás
#     for i in range(b.shape[0]):
#         print(b[i,j], end=" ")
#     print()
######################################################
def is_sorted(vec):
    n = 0
    while vec[n] == vec[n+1]:   #amíg az egymást követő leemek egyenlőek
        n +=1
    if vec[n] < vec[n + 1]:
        for i in range(n + 1,vec.size-1):
            if vec[i] > vec[i + 1]:
                return False
    else:
        for i in range(n + 1, vec.size - 1):
            if vec[i] < vec[i + 1]:
                return False
    return True

def sort_column(mtx, n):
        for i in range(mtx.shape[0] - 1):   #1. sortól az utolsó előttiig
            for j in range(i + 1, mtx.shape[0]):    #2. sortól az utolsóig
                if mtx[i, n] > mtx[j, n]:
                    mtx[i,n], mtx[j,n] = mtx[j, n], mtx[i, n]
        return mtx

def sum_of_mtx(mtx, is_row):
    res = []
    if is_row:
        for i in range(mtx.shape[0]):
            sum = 0
            for j in range(mtx.shape[1]):
                sum +=mtx[i, j]
            res.append(sum)
    else:
        for j in range(mtx.shape[1]):
            sum = 0
            for i in range(mtx.shape[0]):
                sum += mtx[i, j]
            res.append(sum)
    return res

def is_equal_sums(mtx):
    # row_sums = sum_of_mtx(mtx, True)      #1.m.o.
    # col_sums = sum_of_mtx(mtx, False)
    row_sums = np.sum(mtx, axis = 1)    #sorok
    col_sums = np.sum(mtx, axis = 0)    #oszlopok
    # print(mtx)
    # print(row_sums)
    # print(col_sums)
    for i in range(mtx.shape[0]):
        if row_sums[i] != row_sums[0] or col_sums[i] != row_sums[0]:
            return False
    return True

def index_divisors(mtx):
    res = []
    for i in range(mtx.shape[0]):
        for j in range(mtx.shape[1]):
            if mtx[i, j] % (i + 1) == 0 and mtx[i, j] % (j + 1) == 0:
                res.append((mtx[i,j], i + 1, j + 1))
    return res

def check_columns(mtx):
    res = []
    # for j in range(mtx.shape[1]):
    #     zeros = 0
    #     negatives = 0
    #     for i in range(mtx.shape[0])
    #         if mtx[i,j] == 0:
    #             zeros += 1
    #         elif mtx[i,j] < 0:
    #             negatives +=1
    #     if zeros * 2 == negatives:
    #         res.append(j)
    # return res
    for j in range(mtx.shape[1]):   #oszlopfolytonos bejárás
        zeros = np.where(mtx[:,j] == 0)
        negatives = np.where(mtx[:,j] < 0)
        if zeros[0].size * 2 == negatives[0].size:
            res.append(j)
    return res
#  1.feladat:
# a = np.array([2,2,3,4,5])
# print(a)
# print(is_sorted(a))

# 2.feladat:
# b = np.random.randint(1,10,(3,3))
# print(b)
# b = sort_column(b, 1)
# print(b)

# 3.feladat:
# c = np.ones((3,3))
# print(is_equal_sums(c))

# 4.feladat:
# d = np.random.randint(1,10,(3,4))
# print(d)
# print(index_divisors(d))

# 5.feladat:
# n = int(input("Kerem a sorok szamat:"))
# m = int(input("Kerem az oszlopok szamat:"))
#
# e = np.random.randint(-1,1,(n,m))
# print(e)
# print(check_columns(e))