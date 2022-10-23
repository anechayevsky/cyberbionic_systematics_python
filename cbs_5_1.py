fio = input('Введіть ФІО: ' ).split()
for item in fio:
    if item[0].isupper():
        for x in item:
            if not x.isalpha():
                print('Знайдено щось крім літер!!!')
                break
    else:
        print('Кожне слово - з великої літери.')
        break
print(f'Ваше ФІО чудове')