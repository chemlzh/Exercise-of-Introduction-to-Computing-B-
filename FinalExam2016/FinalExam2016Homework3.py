n = int(input())
l = []
x = 2
cnt = 0
print('%d=' % n, end = '')
while n > 1:
    if n % x == 0:
        n /= x
        cnt += 1
        l.append(x)
    else:
        x += 1
for i in range(cnt - 1, -1, -1):
    if i != cnt - 1:
        print('*', end = '')
    print(l[i], end = '')