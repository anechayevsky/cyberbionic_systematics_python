diap = list(map(int, input('Введіть послідовність чисел через пробіл: ').split()))
diap.sort()
print((*diap,))