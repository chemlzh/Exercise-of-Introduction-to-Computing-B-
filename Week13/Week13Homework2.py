s = input()
l = eval(s)
ans = [0, 0, 0, 0]
cnt = 0
for i in range(0, len(l)):
    for j in range(0, 3):
        if l[i][1] > ans[j]:
            for k in range(2, j - 1, -1):
                ans[k + 1] = ans[k]
            ans[j] = l[i][1]
            break
        elif l[i][1] == ans[j]:
            break
for i in range(0, 3):
    if ans[i] == 0:
        break
    else:
        if i == 2:
            print(ans[i], end = '')
        else:
            print(ans[i], end = ' ')