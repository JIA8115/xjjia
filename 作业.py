n = int(input())
if n == 0:
    print(1)
elif n == 1:
    print(0)
else:
    a, b = 1, 0  # 分别代表D(0)和D(1)
    for i in range(2, n + 1):
        c = (i - 1) * (a + b)
        a, b = b, c
    print(b)