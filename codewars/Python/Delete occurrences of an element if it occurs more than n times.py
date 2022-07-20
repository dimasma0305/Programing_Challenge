def delete_nth(order,max_e):
    dc = dict()
    new_order = []
    for i in order:
        if i not in dc:
            dc[i] = 1
        else:
            dc[i] += 1
        if dc[i] <= max_e:
            new_order.append(i)
    return new_order

def delete_nth(order, max_e):
    d = {}
    res = []
    for item in order:
      n = d.get(item, 0)
      if n < max_e:
        res.append(item)
        d[item] = n+1
    return res

print(delete_nth([1,1,3,3,7,2,2,1,1], 3))
