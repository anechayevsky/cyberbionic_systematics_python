diap = list(map(int, input('Введіть діапазон чисел (в діапазоні має бути не менше 5 чисел) через пробіл: ').split()))
print(f'Сума другого, передостаннього, а також середнього арифметичного значення даної послідовності дорівнює '
      f'{diap[1]+diap[-2]+(sum(diap)/len(diap))}')