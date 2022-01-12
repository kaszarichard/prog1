import copy

def print_all_sum_rec(target, current_sum, start, output, result):
    if current_sum == target:
        output.append(copy.copy(result))

    nums_2 = []
    x = 0
    while True: #összegyűjti a 2 hatványait target számig
        i = 2 ** x
        if i <= 10:
            nums_2.append(i)
            x += 1
        else:
            break

    n = 0
    for i in range(start, target, 2**n):
        if i in nums_2:  #csak akkor kezd el dolgozni a számmal, ha az 2 hatványa
            temp_sum = current_sum + i

            if temp_sum <= target:
                result.append(i)
                print_all_sum_rec(target, temp_sum, i, output, result)
                result.pop()

            else:
                return
            n += 1

def print_all_sum(target):
    output = []
    result = []
    print_all_sum_rec(target, 0, 1, output, result)
    return output

def to_sums(res):
    for sum in res:
        if sum:
            curr_sum = ''
            for i in range(len(sum)):

                if i!= len(sum)-1:
                    curr_sum += f'{sum[i]}+'
                else:
                    curr_sum += str(sum[i])

            print(curr_sum)
    print(f'{len(res)} db kombimbináció')


n = int(input("Adj meg egy számot: "))   #bekért szám
res = print_all_sum(n)
to_sums(res)




