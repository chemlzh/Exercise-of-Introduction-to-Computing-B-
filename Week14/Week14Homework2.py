d = [["sir", "matey"], ["hotel", "fleabag inn"], ["student", "swabbie"],
     ["boy",	 "matey"], ["madam", "proud beauty"], ["professor", "foul blaggart"],
     ["restaurant", "galley"], ["your", "yer"], ["excuse", "arr"],
     ["students",	"swabbies"], ["are", "be"], ["lawyer",	"foul blaggart"],
     ["the",	"th’"], ["restroom",	"head"], ["my", "me"],
     ["hello", "avast"], ["is", "be"], ["man", "matey"]]
str = input()
for i in range(0, len(d)):
    pos = 0
    while True:
        pos = str.find(d[i][0], pos)
        if pos != -1:
            str = str[:pos] + d[i][1] + str[pos + len(d[i][0]):]
        else:
            break
print(str)