x = float(input())
d = float(input())
ans = 1.0
f = 1.0
cnt = 1.0
while abs(x ** cnt / f) >= d:
    ans = ans + x ** cnt / f
    cnt = cnt + 1.0
    f = f * cnt
print(round(ans, 6))