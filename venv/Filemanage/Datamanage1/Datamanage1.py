#open data file
openfile = open('task_file.txt')

#transform data to string
data = str(openfile.read())

#remove first row and transform data to list
data_spec = str(data.split('\n, ')[0])
data_1 = data.split('\n, ')[1:]

#define inputs for email gen
def inputs(x):
    row = str(data_1[x])
    row = row.split(', ')
    return [[row[0], row[1]]]

#define list of names for email gen
list_of_names = []
for x in range(len(data_1)):
    list_of_names += inputs(x)

#email generator
def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0] + str(letter) + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails


#define name, surname, phone, adress in rows
def personal_data_row(x):
    row = str(data_1[x])
    row = row.split(', ')
    return str(row[0]) + ', ' + str(row[1]) + ', ' + str(row[2]) + ', ' + str(row[3])

#define email row
def email_row(x):
    row = str(data_1[x])
    row = row.split(', ')
    if row[0] and row[1] and row[2] and row[3] != ' ' and len(row[2]) == 7 and row[2].isnumeric():
        column_mail = str(email_gen(list_of_names)[x])
    else:
        column_mail = ''
    return column_mail

#define new data row
def new_data_row(x):
    new_row = email_row(x) + ', ' + personal_data_row(x)
    return new_row

#Print table with new data
new_data = ''
for x in range(len(data_1)):
     new_data += new_data_row(x) + '\n'
new_data = data_spec + '\n' + new_data

print(new_data)

openfile.close()


