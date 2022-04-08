def lonelyinteger(a):
    set_a = set(a)
    for i in set_a:
        if a.count(i) == 1:
            return i

if __name__ == '__main__':
    print(lonelyinteger([1,1,2,2,3]))