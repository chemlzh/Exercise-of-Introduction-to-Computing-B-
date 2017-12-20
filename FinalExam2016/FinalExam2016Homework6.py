def stat(str, num):
    if str in d:
        d[str] += num
    else:
        d[str] = num


a = input()
b = input()
if len(a) != len(b):
    print('No')
else:
    cnt = len(a)
    flag = 1
    d = {}
    for i in range(0, cnt): 
        stat(a[i], 1)
        stat(b[i], -1)
    for i in d:
        if d[i] != 0:
            print('No')
            flag = 0
            break
    if flag:
        print('Yes')