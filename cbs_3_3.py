a, b, c = map(float, input("Для розв'язання квадратного рівняння, будь ласка, введіть значення 'a', 'b' і 'c' через пробіл: ").split())
d = b**2 - 4 * a * c
x1 = (-b + d**0.5)/2*a
x2 = (-b - d**0.5)/2*a
if d < 0:
    print('Немає дійсних коренів')
elif d == 0:
    print(f'x = {x1}')
else:
    print(f'x1 = {x1}, x2 = {x2}')

