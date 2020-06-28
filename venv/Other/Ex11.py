n = int(input('Enter n: '))
if n < 0 or n > 9:
    print("n must be from 0 to 9")

else:
    for i in range(int(n)):
        x = 0
        y = i + 1
        z = n - i
        while z > 1:
            z -= 1
            print(' ', end='')
        while x <= i:
            x += 1
            print(x, end='')
        print('')
    for j in range(int(n)):
        x = 0
        y = n - j + 1
        while x < n:
            x += 1
            print(' ', end='')
        while y > 1:
            y -= 1
            print(y, end='')
        print('')