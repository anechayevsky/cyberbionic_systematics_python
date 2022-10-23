list_1 = list(map(int, input('Для першого списку, введіть послідовність чисел через пробіл: ').split()))
list_2 = list(map(int, input('Для другого списку, введіть послідовність чисел через пробіл: ').split()))
list_result = []
for item in list_1:
        if (item not in list_2) and (item not in list_result):
            list_result.append(item)
for item in list_2:
        if (item not in list_1) and (item not in list_result):
            list_result.append(item)
res_sort = sorted(list_result)
res_sort_reverse = sorted(list_result, reverse=True)
print(f'Результат в прямій послідовності: {list_result} \n'
      f'Результат в зворотній послідовності: {list_result[::-1]} \n'
      f'Результат відсортований за зростанням: {res_sort} \n'
      f'Результат відсортований за спаданням: {res_sort_reverse} \n')



