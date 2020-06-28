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
count = []
for x in range(1, (len(data_1))):
    count += [inputs(x)]
    list_of_names = count


#create data array
#data_array = []
#for x in range(len(data_1)):
    #data_array = name(x)
    #print(data_array)




#create list of names
    #list_of_names = [[data_array[0]] + [data_array[1]]]
    #print(list_of_names)


#create email generator
    def email_gen(list_of_names):
        emails = []
        for i in list_of_names:
            letter = 1
            while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
                letter += 1
            emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
        return emails


    print(email_gen(list_of_names))

    openfile.close()


