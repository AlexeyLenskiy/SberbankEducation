list_1 = [1,2,3,4,5,6,7]
list_2 = [10,2,3,4,8]

set_1 = set(list_1)
set_2 = set(list_2)
all = set_1.intersection(set_2)
count = len(all)
print(count)