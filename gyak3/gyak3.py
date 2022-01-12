# 1.feladat:
import sys
def list_fill(args):
    list1 = []
    list2 = []
    is_second_list = False
    for arg in args:
        if arg == 'L:':
            is_second_list = True
        else:
            if is_second_list:
                list2.append(arg)
            else:
                list1.append(arg)
    return list1, list2
def  list_subtraction(list1, list2):
    output = []
    for item in list1:
        if item not in list2:
            output.append(item)
    return output

list1, list2 = list_fill(sys.argv[2:])
print(list1)
print(list2)
output = list_subtraction(list1, list2)
print(output)

# 2.feladat:
def sum_numbers(n, out_file):
    sum = 0
    for i in range(1, n):
        sum += i
        print(f"{i}+", file=out_file, end="")
    sum += n
    print(f"{n}={sum}", file=out_file)
import sys
n = int(sys.argv[1])
filename = sys.argv[2]

out_file = open(filename, "n")
sum_numbers(n, out_file)
out_file.close()

# 3.feladat:
def convert_int_to_date(n):
    year = n//(365 * 24 * 3600)
    n = n % (365 * 24 * 3600)

    month = n // (3600 * 24 * 30)
    n = n %(3600 * 24 *30)

    day = n//(3600*24)
    n = n % (3600 * 24)

    hour = n//3600
    n = n%3600

    minute = n//60
    n = n % 60

    second = n
    return f"{year}, {month}, {day}, {hour}, {minute}, {second}"
n = int()

# 4.feladat:
import sys
def sum_of_string(string):

    curr_number = ""
    sum = 0
    for ch in string:
        if ch.isdigit():
            curr_number += ch
        elif len(curr_number) > 0:
            sum += int(curr_number)
            curr_number = ""
    if len(curr_number) > 0:
        sum += int(curr_number)
    return sum

print("The sum of {".format(sys.argv[1],sum_of_string((sys.argv[1]))))


# 5.feladat:
import sys,random
def sum_random(args):
    n = int(args[0])
    file_name = args[1]
    sum = 0
    out_file = open(file_name,"w")
    for i in range(n):
        num = random.randint(1,100)
        sum += num
        print(num, file=out_file)
    print("Szamok osszege: {}".format(sum), file=out_file)
    out_file.close()

sum_random(sys.argv[1:])