from functools import reduce
import operator


def persistence(n):
    print(n)
    if len(str(n)) == 1:
        return 0
    count = 0
    while len(str(n)) > 1:
        n = [int(i) for i in str(n)]
        mult = 1
        for i in n:
            mult *= i
        count += 1
        n = mult
    return count


def persistence(n):
    i = 0
    while n >= 10:
        n = reduce(operator.mul, [int(x) for x in str(n)], 1)
        i += 1
    return i



print(persistence(9999999))
