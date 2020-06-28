s = 'Abracadabra'

print(s[2])
print(s[-2])
print(s[0:5])
print(s[0:-2])

x = 0
print(s[x], end='')
while x < len(s) - 2:
    x += 2
    print(s[x], end='')
print('')


y = 1
print(s[y], end='')
while y < len(s) - 2:
    y += 2
    print(s[y], end='')
print('')


z = len(s)
while z > 0:
    z -= 1
    print(s[z], end='')
print('')


f = len(s) - 1
print(s[-1], end='')
while f > 0:
    f -= 2
    print(s[f], end='')
print('')


print(len(s))