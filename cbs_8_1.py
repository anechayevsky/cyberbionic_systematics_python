def hello(name='Віталій'):
    print('Hello, ', name, '!', sep='')


def main():
    name = input("Введіть будь ласка ім'я: ")
    return hello(name) if name else hello()


if __name__ == '__main__':
    main()
