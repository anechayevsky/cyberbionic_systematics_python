def diap_sum(start, stop):
    return start if start == stop else diap_sum(start + 1, stop) + start

def main():
    a, b = map(int, input('Введіть начало та кінець діапазона через пробіл: ').split())
    print(f'Сумма натуральних натуральних чисел, які входять до заданого проміжку, складає {diap_sum(a,b)}')

if __name__ == '__main__':
    main()
