openfile = open('task_file.txt')
data = str(openfile.read())
data_1 = (data.split('\n, '))

#divide parameters in each string
def name(x):
    data_x = data_1[x]
    return (data_x.split(', '))

#create inputs
def inputs(x):
    inputs = [name(x)[0], name(x)[1]]
    return (inputs)

#create list of names
list_of_names = []
for x in range(1, (len(data_1))):
    list_of_names += [inputs(x)]
print(list_of_names)

#email generator
def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter+=1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails

print(email_gen(list_of_names))

openfile.close()


