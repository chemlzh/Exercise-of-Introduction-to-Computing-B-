import random


def testqs():
    lst = []
    for i in range(100):
        lst.append(random.randint(1,200))
    print(lst)
    testlst = lst
    sortedlst = qs(testlst, 0, len(testlst) - 1)
    assert(sorted(lst) == sortedlst)
    print('Test pass')


def qs(lst, left, right):
    '''quick sort list lst, return the sorted list'''
    mid = (left + right) // 2
    key = lst[mid]
    l = left
    r = right
    while l <= r:
        while lst[l] < key:
            l += 1
        while lst[r] > key:
            r -= 1
        if l <= r:
            tmp = lst[l]
            lst[l] = lst[r]
            lst[r] = tmp
            l += 1
            r -= 1
    if r > left:
        qs(lst, left, r)
    if l < right:
        qs(lst, l, right)
    return lst[left:right + 1]


def main():
    testqs()


if __name__ == "__main__":
    main()