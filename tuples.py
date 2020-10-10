def tupl(a):
    b = []
    for i in range(0, len(a)):
        if i % 2 == 0:
            b.append(a[i] * 2)
        else:
            b.append(a[i] - 2)
    b = tuple(b)
    print(b)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
tupl(a)