```python
def int32_to_ip(int32):
    return '.'.join([str(int32 >> i & 0xFF) for i in [24, 16, 8, 0]])

print(int32_to_ip(3123123))
```