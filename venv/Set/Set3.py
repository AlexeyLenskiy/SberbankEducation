#set_1 = {1, 2, 3}
#set_2 = {1, 4, 5}
set_1 = {1, 2, 3, 4, 5, 6, 7}
set_2 = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0}
#set_1 = {1, 10, 223, 413, 2}
#set_2 = {1, 10, 223, 413, 2}

if set_1.issubset(set_2) and set_1 != set_2:
    print(True)
else:
    print(False)


