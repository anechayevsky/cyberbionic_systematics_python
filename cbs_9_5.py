def quadratic_equation(a, b, c):
    x1 = None
    x2 = None

    def calc_rezult(a, b, c, x1, x2):
        d = b ** 2 - 4 * a * c
        if d > 0:
            x1 = (-b + d ** 0.5) / 2 * a
            x2 = (-b - d ** 0.5) / 2 * a
        elif d == 0:
            x1 = - b / 2 * a
        return x1, x2

    result = calc_rezult(a, b, c, x1, x2)
    return result

def main():
    a, b, c = map(float, input("Для розв'язання квадратного рівняння, будь ласка, введіть значення 'a', 'b' і 'c' через пробіл: ").split())
    result = quadratic_equation(a, b, c)
    print(f'Коренями рівняння є: {result[0]} та {result[1]}')

if __name__ == '__main__':
    main()
