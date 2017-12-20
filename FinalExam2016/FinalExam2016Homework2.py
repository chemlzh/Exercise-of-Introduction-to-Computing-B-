p = input().split()
q = sorted(list(map(lambda x: int(x), p)))
l = len(q)
if l % 2 == 0:
    print((q[l // 2] + q[l // 2 - 1]) / 2)
else:
    print(q[l // 2])