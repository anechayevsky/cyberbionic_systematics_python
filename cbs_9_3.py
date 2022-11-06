def stairs(n):
    if n == 1 or n == 2:
        return 1
    else:
        return stairs(n - 1) + stairs(n - 2)


def main():
    n = int(input('На яку сходинку бажаєта піднятися? '))
    print(f'Ви можете це зробити {stairs(n+1)} способами')


if __name__ == '__main__':
    main()
