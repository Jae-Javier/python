a, b = 0, 1
while a < 12 or a == 12:
    print(a, end=',')
    print(b, end=',')
    print((a+b))
    a, b = b, a + b
