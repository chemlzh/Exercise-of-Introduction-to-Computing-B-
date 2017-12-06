str = input()
for i in range(0, len(str)):
    if 'A'<= str[i] <= 'Z':
        pos = (ord(str[i]) - ord('A') +13) % 26
        print(chr(pos + ord('A')), end = '')
    elif 'a' <= str[i] <= 'z':
        pos = (ord(str[i]) - ord('a') +13) % 26
        print(chr(pos + ord('a')), end = '')
    else:
        print(str[i], end = '')