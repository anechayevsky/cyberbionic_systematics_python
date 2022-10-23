int_list = list(map(int, input('Введіть натуральні числа для створення списку: ').split()))
new_list = []
for item in int_list:
    if not item % 2 == 0:
        new_list.append(item)
repeat = int(input('Скільки разів бажаєте продублювавати новий список? '))
repeat_list = []
for item in new_list:
    for i in range(repeat):
        repeat_list.append(item)
print(f'Перший варіант дублювання: {repeat_list}')
repeat_2 = []
for i in range(repeat):
    repeat_2.append(new_list)
print(f'Другий варіант дублювання: {repeat_2}')
repeat_3 = []
for i in range(repeat):
    for item in new_list:
        repeat_3.append(item)
print(f'Третій варіант дублювання: {repeat_3}')
int_list.clear()