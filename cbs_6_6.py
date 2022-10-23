int_list = list(map(int, input('Введіть натуральні числа для створення списку: ').split()))
new_list = []
for item in int_list:
    if not item % 2 == 0:
        new_list.append(item)
repeat = int(input('Скільки разів бажаєте продублювавати новий список? '))
repeat_1 = []
for item in new_list:
    for i in range(repeat):
        repeat_1.append(item)
print(f'Перший варіант дублювання: {repeat_1}')
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
number = int(input('Яке число потрібно шукати? '))
var = int(input('В якому варіанті дублювання: "1", "2" чи "3"? '))
if var == 1:
    print(f'Це число повторюється {repeat_1.count(number)} разів, а його позиція - {repeat_1.index(number)}')
elif var == 3:
    print(f'Це число повторюється {repeat_3.count(number)} разів, а його позиція - {repeat_3.index(number)}')
elif var == 2:
    print(f'Це число повторюється {len(repeat_2)} разів, а його позиція - {repeat_2[0].index(number)}')