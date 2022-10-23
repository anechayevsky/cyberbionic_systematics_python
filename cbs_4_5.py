height = int(input('Введіть висоту прямокутника: '))
width = int(input('Введіть ширину прямокутника: '))
print('Ось ваш прямокутник:')
for i in range(height):
    for j in range(width):
        print(' * ', end='')
    print()