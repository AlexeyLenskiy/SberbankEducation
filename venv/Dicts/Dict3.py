list_1 = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
dict_1 = {}.fromkeys(list_1, 0)
for i in list_1:
    dict_1[i] += 1
list_2 = list(dict_1.values())
for i in range(len(list_2)):
    result = list_2[i]
    print(result, end="")


