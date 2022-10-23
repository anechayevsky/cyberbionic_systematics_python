example = list(map(int, input('Введіть послідовність чисел через пробіл: ').split()))
example.sort()
print(f'Найбільший елемент списку: {example[-1]} \n'
      f'Найменьший елемент списку: {example[0]} \n'
      f'Сума елементів списка: {sum(example)} \n'
      f'Середнє арифметичне: {sum(example)/len(example)}')

