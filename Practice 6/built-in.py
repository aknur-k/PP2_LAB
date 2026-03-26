nums = [1, 2, 3, 4]

print(len(nums))   # 4
print(sum(nums))   # 10
print(min(nums))   # 1
print(max(nums))   # 4

# map() :
nums = [1, 2, 3]
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1, 4, 9]

# filter()
nums = [1, 2, 3, 4]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # [2, 4]

# reduce()
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x*y, nums)
print(product)  # 24


# enumerate()
names = ["A", "B", "C"]

for i, name in enumerate(names):
    print(i, name)


# zip()
a = [1, 2, 3]
b = ["a", "b", "c"]

print(list(zip(a, b)))
# [(1, 'a'), (2, 'b'), (3, 'c')]


# sorted()
nums = [4, 1, 3]
print(sorted(nums))          # [1, 3, 4]
print(sorted(nums, reverse=True))  # [4, 3, 1]


# type conversion
print(int("5"))
print(float("3.14"))
print(str(10))
print(list("abc"))
