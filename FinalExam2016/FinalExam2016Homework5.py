def flatten_list(l0):
    for i in l0:
        if type(i) == list:
            flatten_list(i)
        else:
            newl.append(i)


l = eval(input())
newl = []
flatten_list(l)
print(newl)