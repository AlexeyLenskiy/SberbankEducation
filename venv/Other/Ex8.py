mass = [0,1,2,3,4,5,6,7,8,9]


def find_sum(mass):
    #Вставьте свой код ниже
    sum = 0
    for n in range(10):
      sum += mass[n]
    return sum

print(find_sum(mass))