def imt(height, weight):
    return weight / (height ** 2)


def main():
    print('Будемо розраховувати ваш індекс маси тіла!\n')
    while True:
        option = input('Якщо бажаєте завершити роботу програми, наберіть "off", якщо ні - будь-що :) \n')
        if option == 'off':
            print('\nДо побачення!')
            break
        height = int(input('Введіть ваш зріст у сантиметрах: '))
        weight = int(input('Введіть вашу вагу у кілограмах: '))
        result = imt(height / 100, weight)
        if result < 18.5:
            print(f'\nВаш індекс маси тіла складає {result:.2f}, ваша вага занизька\n')
        elif 18.5 <= result <= 24.9:
            print(f'\nВаш індекс маси тіла складає {result:.2f}, це чудово! Ви неперевершані!\n')
        elif 24.9 < result:
            print(f'\nВаш індекс маси тіла складає {result:.2f}, це забагато. Слідкуйте за фігурою\n')


if __name__ == '__main__':
    main()
