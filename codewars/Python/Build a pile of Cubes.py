def find_nb(m):
    total = 0
    n = 0
    while total < m:
        n += 1
        total += n**3
    return n if total == m else -1
            
print(find_nb(135440716410000))