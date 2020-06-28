n = int(input('Enter n: '))


for i in range(int(n)):
    x = 0
    while x <= i:
        x += 1
        print(x, end='')
        if x > i:
            print('')


