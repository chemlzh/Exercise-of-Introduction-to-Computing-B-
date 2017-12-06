import re
str = input()
ans = 0
words = re.split('[ ,.;?!\t]', str)
for i in range(0, len(words)):
    if words[i] == '':
        continue
    flag = True
    l = len(words[i])
    for j in range(0, int(l / 2)):
        if words[i][j] != words[i][l - j - 1]:
            flag = False
            break
    if flag == True:
        ans += 1
print(ans)