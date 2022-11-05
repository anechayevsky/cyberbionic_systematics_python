def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return 'На нуль ділити не можна'
    return a / b


def grade(a, b):
    return a ** b


def square(a):
    return a ** 0.5


def cube(a):
    return a ** (1. / 3.)


def main():
    print('Вітаємо в калькуляторі!')
    while True:
        option = input('Яку операцію хочете здійснити (введіть число): \n'
                       '1. Додавання \n'
                       '2. Віднімання \n'
                       '3. Множення \n'
                       '4. Ділення \n'
                       '5. Зведення в ступінь \n'
                       '6. Зведення до квадратного коріня \n'
                       '7. Зведення до кубічного коріня \n\n'
                       '0. Завершити роботу \n')

        match option:
            case '1':
                a = float(input('Введіть перше число: '))
                b = float(input('Введіть друге число: '))
                print(f'{a} + {b} = {plus(a, b)} \n')

            case '2':
                a = float(input('Введіть перше число: '))
                b = float(input('Введіть друге число: '))
                print(f'{a} - {b} = {minus(a, b)} \n')

            case '3':
                a = float(input('Введіть перше число: '))
                b = float(input('Введіть друге число: '))
                print(f'{a} х {b} = {mult(a, b)} \n')

            case '4':
                a = float(input('Введіть перше число: '))
                b = float(input('Введіть друге число: '))
                if b == 0:
                    print('На нуль ділити не можна')
                else:
                    print(f'{a} / {b} = {div(a, b)} \n')

            case '5':
                a = float(input('Введіть перше число: '))
                b = float(input('В яку ступінь звести? '))
                print(f'{a} ** {b} = {grade(a, b)} \n')

            case '6':
                a = float(input('З якого числа квадратний корінь? '))
                print(f'Квадратни корінь з {a} дорівнює {square(a)} \n')

            case '7':
                a = float(input('З якого числа кубічний корінь? '))
                print(f'Кубічний корінь з {a} дорівнює {cube(a)} \n')

            case '0':
                print(f'До побачення!')
                break

            case _:
                print('Щось не те ви ввели, спробуйте ще раз. \n')


if __name__ == '__main__':
    main()
