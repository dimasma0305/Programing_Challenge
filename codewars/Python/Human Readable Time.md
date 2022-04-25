```python
def make_readable(seconds):
    SS = seconds % 60
    MM = seconds // 60 % 60
    HH = seconds // 3600
    return '{:02d}:{:02d}:{:02d}'.format(HH, MM, SS)

print(make_readable(123123123))
```