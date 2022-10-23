from functools import reduce
a, n = map(int, input('Введіть начало та кінець діапазону через пробіл: ').split())
lst = []
for i in range(3, n + 1, 2):
    if (i > 10) and (i % 10 == 5):
        continue
    for j in lst:
        if j * j - 1 > i:
            lst.append(i)
            break
        if (i % j == 0):
            break
    else:
        lst.append(i)
index = 0
for item in lst:
    if item >= a:
        break
    index +=1
print(f'{lst[index:]}')
action = int(input('Якщо бажаєте розрахувати суму ціх чисел, натисніть "1", якщо добуток - натисніть "2" '))
if action == 1:
    print(f'Сума складає: {sum(lst)}')
elif action == 2:
    result = reduce(lambda x,y: x*y, lst)
    print(f'Добуток складає: {result}')
