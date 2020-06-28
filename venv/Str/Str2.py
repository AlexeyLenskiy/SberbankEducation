#s = 'ivan ivanov'
#s = 'can    you   solve  it?'
#s = 'abraсadabra'
#s = 'a1 2b  3   abc d3e r2D2'
s = input('')

s = s.lower()
x = s.upper()
x = x[0]
y = s[1:-1]
print(x, end = '')
for i in range(len(y)):
   if y[i - 1] != ' ':
    print(y[i], end = '')
   elif y[i - 1] == ' ':
    y1 = y[i]
    y1 = y1.upper()
    print(y1, end ='')
if s[-2] != ' ':
    print(s[-1])
elif s[-2] == ' ':
 s = s.upper()
 print(s[-1])
