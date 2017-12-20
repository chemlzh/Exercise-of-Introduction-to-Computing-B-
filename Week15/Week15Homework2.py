newd = {}

def trans(com, p):
    if type(com[1]) == dict:
        for i in com[1].items():
            trans(i, p + com[0] + '.')
    elif p == '':
        newd[com[0]] = com[1]
    else:
        newd[p + com[0]] = com[1]


def flatten_dict(d0):
    for i in d0.items():
        trans(i, '')
    print(newd)


def main():
    d = eval(input())
    flatten_dict(d)


if __name__ == '__main__':
    main()