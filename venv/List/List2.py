list_1 = list('12345')
even_list = []
for n in range(len(list_1)):
  if list_1[n] > list_1[n - 1] and n != 0:
    even_list.append(list_1[n])

print(list_1)
print(even_list)
