list_1 = [-5, 5, 10]
list_2 = list_1.copy()
new_list = list_1
ma = max(list_2)
mi = min(list_2)
imax = list_2.index(ma)
imin = list_2.index(mi)
new_list.insert(imax, mi)
del (new_list[imax + 1])
new_list.insert(imin, ma)
del (new_list[imin + 1])

print(new_list)