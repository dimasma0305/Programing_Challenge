```python
def is_prime(num):
    # optimize for system performance
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    if num < 9:
        return True
    if num % 3 == 0:
        return False
    r = int(num ** 0.5)
    f = 5
    while f <= r:
        if num % f == 0:
            return False
        if num % (f + 2) == 0:
            return False
        f += 6
    return True
```