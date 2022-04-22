```python
def square_digits(num):
    num = [int(i) for i in str(num)]
    return int(''.join([str(i*i) for i in num]))
print(square_digits(9119))
```