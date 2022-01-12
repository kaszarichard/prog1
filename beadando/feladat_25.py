import numpy as np
import random

def prime_nums(end):

    prime = set(range(2, end + 1))
    p = 2

    while 2 <= p < end:
        while p not in prime and 2 <= p < end:
            p = p + 1
        k = p + p
        while k < end:
            if k in prime:
                prime.remove(k)
            k = k + p
        p = p + 1
    return list(prime)

def n_random_vec(n, size, start, end):
    prime_lst = prime_nums(end)
    for i in range(n):
        prime_db = 0
        even_db = 0
        odd_db = 0
        curr_prime_lst =[]
        curr_even_lst = []
        curr_odd_lst = []
        curr_vec = np.random.randint(start, end, size)

        for num in curr_vec:
            if num in prime_lst:
                prime_db += 1
                curr_prime_lst.append(num)
            elif num%2!=0:
                curr_odd_lst.append(num)
                odd_db += 1
            else:
                curr_even_lst.append(num)
                even_db += 1

        if prime_db >= 2:
            nums_type = "(Prím számok) "
            res_vec = curr_prime_lst
            curr_prime_lst = []
        elif prime_db < 2 and odd_db >= 2:
            nums_type = "(Páratlan számok) "
            res_vec = curr_odd_lst
            curr_odd_lst = []
        elif prime_db < 2 and odd_db < 2:
            nums_type = "(Páros számok) "
            res_vec = curr_even_lst
            curr_even_lst = []

        prime_db = 0
        even_db = 0
        odd_db = 0

        res_str = ""
        for j in range(len(res_vec)):
            op_lst = ['+', '-', '*', '//']
            idx_op = random.randint(0, 3)
            if j == len(res_vec)-1:
                res_str += str(res_vec[j])
            else:
                res_str += str(res_vec[j]) + op_lst[idx_op]

        res = eval(res_str)
        print(f'{nums_type}{res_str} = {res}')
        res_str =''
        res_vec = []

size = int(input('Random vektorok mérete: '))
db = int(input("Random vektorok száma: "))
start = int(input("Random vektorok kezdő értéke: "))
end = int(input("Random vektorok végértéke: "))
n_random_vec(size, db, start, end)

