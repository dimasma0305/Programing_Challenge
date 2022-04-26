```python
def max_sequence(arr):
    max_ending_here = max_so_far = 0
    for x in arr:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
```