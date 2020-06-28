var_1 = input("Enter var1: ")
var_2 = input("Enter var2: ")
var_3 = input("Enter var3: ")

def find_equal(var_1, var_2, var_3):
    if var_1 == var_2 and var_1 == var_3:
        count = 3
    elif var_1 == var_2 or var_1 == var_3 or var_2 == var_3:
        count = 2
    else:
        count = 0
    return count

print(find_equal(var_1, var_2, var_3))