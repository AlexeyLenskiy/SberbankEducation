mass = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

def find_null(mass):
    sum = 0
    for n in range(len(mass)):
        if mass[n] == 0:
            sum += 1

    return sum
print(find_null(mass))