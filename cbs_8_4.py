def average(a, b, c):
    return (a + b + c) / 3


def main():
    while True:
        a, b, c = map(float, input('Введіть три числа через пробіл: ').split())
        print(f'Середнє арифметичне дорівнює: {average(a, b, c)}')
        option = input('Якщо бажаєте завершити роботу, наберіть "off" чи будь-що, якщо бажаєте продовжувати')
        match option:
            case 'off':
                print('До побачення!')
                break


if __name__ == '__main__':
    main()
