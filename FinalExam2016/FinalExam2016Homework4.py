def trans(num):
    ans = 0
    while num > 0:
        ans += num % 10
        num = num // 10
    return ans


n = int(input())
while n >= 10:
    n = trans(n)
print(n)