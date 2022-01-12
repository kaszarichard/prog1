lst = [2,3,4,8,2,3]
#print(lst)
s1 = set(lst)
#print(s1)
# for item in s1:
#     print(item)
#
# s1.add(9)
# print(s1)
#
# s1.remove(4)
# print(s1)
s2 = {3,5,9,8,1}

#unio
#unio = s1.union(s2)
unio = s1 | s2
print(unio)

#intersection
#inter = s1.intersection(s2)
inter = s1 & s2
print(inter)

#difference
print("elso halmaz: {}".format(s1))
print("masodik halmaz: {}".format(s2))
#diff = s1.difference(s2)
diff = s1 - s2
print("kulonbseg: {}".format(diff))

#simmertric difference
#s_diff = s1.symmetric_difference(s2)
s_diff = s1 ^ s2
print("symmertic difference: {}".format(s_diff))