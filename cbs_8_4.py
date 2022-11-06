
def main():
    while True:
        numbers = [int(value) for value in input('Введіть будь-яку кількість чисел через пробіл: ').split()]
        print(f'Середнє арифметичне дорівнює: {sum(numbers)/len(numbers)}')
        option = input('Якщо бажаєте завершити роботу, наберіть "off" чи будь-що, якщо бажаєте продовжувати')
        match option:
            case 'off':
                print('До побачення!')
                break


if __name__ == '__main__':
    main()
