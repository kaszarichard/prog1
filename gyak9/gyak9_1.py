import math

# def area(r):
#     return r**2 * math.pi

area = lambda r : r**2 * math.pi

radius = [1,2,3,4,5]

res = list(map(area, radius))

print(radius)
print(res)