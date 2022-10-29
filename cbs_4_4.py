a, b = map(int, input('Введіть числа "а" и "b" через пробіл: ').split())
list = [i for i in range(a,b+1)]
average = sum(list)/len(list)
print(sum(list))
print(average)
result = 0
for item in list:
    if item%average == 0:
        result += item
print(f'Cума всіх натуральних чисел від a до b (включно), які є кратними середньому арифметичному цього проміжку дорівнює {result}')