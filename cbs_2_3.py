a, b, c = map(float, input("Для розв'язання квадратного рівняння, будь ласка, введіть значення 'a', 'b' і 'c' через пробіл: ").split())
d = b**2 - 4 * a * c
x1 = (-b + d**0.5)/2*a
x2 = (-b - d**0.5)/2*a
print(f'x1 = {x1}, x2 = {x2}')


