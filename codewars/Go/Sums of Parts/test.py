def parts_sums(ls):
    sums = [0] * (len(ls) + 1)
    for i, e in enumerate(reversed(ls)):
        sums[len(ls) - i - 1] += sums[len(ls) - i] + e
        print(i, e)
    return sums

print(parts_sums([1,2,3,4]))