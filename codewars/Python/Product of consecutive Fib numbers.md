```python
def productFib(prod):
    n = 0
    nPlus = 1
    while n * nPlus < prod:
        nPlus = n +nPlus
        n = nPlus - n
    return [n, nPlus, n * nPlus == prod]
    
print(productFib(123))
```

```python
def productFib(prod):
    func = lambda a, b: func(b, a+b) if a*b < prod else [a, b, a*b == prod]
    return func(0, 1)
```