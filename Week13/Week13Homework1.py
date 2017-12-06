s = input()
l = s.split()
ans = 0
for i in range(0, len(l)):
    if l[i].isdigit() == True and  int(l[i]) % 2 == 0:
        ans += int(l[i])
print(ans)