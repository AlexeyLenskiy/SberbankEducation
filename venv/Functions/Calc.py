expression = input()
pow = expression.replace('**', ' ** ')
mult = pow.replace('*', ' * ')
add = mult.replace('+', ' + ')
sub = add.replace('-', ' - ')
div = sub.replace('/', ' / ')
s = div.split(' ')
for i in range(len(s)):
    s.remove('')
    print(s)
    








