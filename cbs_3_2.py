from math import pi, cos
x = float(input('Введіть будь ласка значення "x" в діапазоні -𝜋 <= x <= 𝜋, а я порахую cos(3x) '))
if -pi <= x <= pi:
    print(f'cos(3x) = {cos(3*x)}')
else:
    print('Значення "х" не в діапазоні -𝜋 <= x <= 𝜋')
