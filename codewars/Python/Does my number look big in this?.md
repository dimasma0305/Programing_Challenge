```python
def narcissistic( value ):
    # pisahkan value menjadi list
    value_now = [int(i) for i in list(str(value))]
    total = 0
    for i in value_now:
        total += i ** len(value_now)
    if total == value:
        return True
    else:
        return False
        

if __name__ == '__main__':
    print(narcissistic( 371 ))
```
