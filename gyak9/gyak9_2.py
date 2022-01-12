nums = [5, 6, 47, 54, 80, 66]

oszthato_e = lambda n : True if n % 6 == 0 else False

res = list(filter(oszthato_e, nums))

print(nums)
print(res)