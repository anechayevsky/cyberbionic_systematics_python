int_list = list(map(int, input('Введіть натуральні числа для створення списку: ').split()))
action = int(input('Якщо бажаєте цей список в зворотньому порядку, натисніть "1", якщо за зростанням - "2": '))
if action == 1:
    print(*int_list[::-1])
elif action == 2:
    print(*sorted(int_list))
