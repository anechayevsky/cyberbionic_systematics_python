def palindrom(text):
    print('Так, це паліндром!') if text.lower().replace(' ','') == text.lower().replace(' ','')[::-1] else print(
        'Ні, це не паліндром')


def main():
    text = input('Введіть текст, який будемо провіряти на поліндромність: ')
    palindrom(text)

if __name__ == '__main__':
    main()