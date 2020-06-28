var_1 = input("Enter var1: ")
var_2 = input("Enter var2: ")
var_3 = input("Enter var3: ")

def find_min(var_1, var_2, var_3):
    if var_1 <= var_2 and var_1 <= var_3:
        min = var_1
    elif var_2 < var_1 and var_2 < var_3:
        min = var_2
    else:
        min = var_3
    return min

print(find_min(var_1, var_2, var_3))