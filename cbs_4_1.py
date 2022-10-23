from functools import reduce
a, b = map(int, input('Введіть числа "а" и "b" через пробіл: ').split())
print(reduce(lambda x,y:x+y, range(a,b+1)))