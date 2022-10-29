def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)

n = int(input('Введіть, будь ласка, число, для якого потрібно обчислити факторіал: '))
print(f'Факторіал числа {n} дорівнює {factorial(n)}')