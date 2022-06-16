```python
class add(int):__call__ = lambda self, v: add(self+v)

print(add(1)(2)(3))
```

```python
class add(int):
    def __call__(self,n):
        return add(self+n)
```