def check(a, b, c):
    return (a ** 2) + (b ** 2) == c ** 2


a = 1
b = 2
while True:
    c = 1000 - a - b
    if check(a, b, c):
        break
    if b + 1 < c:
        b += 1
    else:
        a += 1
        b = a + 1


print("{} {} {} ".format(a, b, c))
print(a * b * c)
