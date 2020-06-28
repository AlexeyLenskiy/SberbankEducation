list_1 = list('12345')
even_list = []
for n in range(len(list_1)):
  if n % 2 == 0:
    even_list.append(list_1[n])
print(list_1)
print(even_list)