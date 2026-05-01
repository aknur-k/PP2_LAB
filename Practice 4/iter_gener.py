def squares(n):
    for i in range(1, n + 1):
        yield i * i


n = int(input())
for num in squares(n):
    print(num)


def generator(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

n = int(input())

first = True
for num in generator(n):
    if not first:
        print(",", end = "")
    print(num, end = "")
    first = False


def generator(n):
    for i in range(0, n + 1):
        if i % 12 == 0:
            yield i

n = int(input())

for num in generator(n):
    print(num)



def generator(a, b):
    for i in range(a, b + 1):
        yield (i ** 2)

a, b = map(int, input().split())

for num in generator(a, b):
    print(num)


def a(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())

for num in a(n):
    print(num)