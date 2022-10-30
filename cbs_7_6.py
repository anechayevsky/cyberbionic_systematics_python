print('Welcome to our library!')
books = {'Кінг': 'Воно', 'Лондон': 'Білий клик', 'Керролл': 'Аліса у країні чудес',
         'Ліндгрен': 'Карлсон, який живе на даху', 'Дефо': 'Пригоди Робінзона Крузо',
         'Дюма': 'Граф Монте Крісто'}

while True:
    menu = input(
                'Please select the action you wish to take: \n'
                '1. View a list of authors \n'
                '2. View a list of books \n'
                '3. Add author and book \n'
                '4. Finish work\n')
    match menu:
        case '1':
            sorted_books =dict(sorted(books.items()))
            for key, value in sorted_books.items():
                print(key)
            print()
        case '2':
            list_books = [value for key,value in books.items()]
            print(*sorted(list_books), sep='\n')
            print()
        case '3':
            author = input("Enter the author's name: ")
            book = input("Enter the book's title: ")
            books[author] = book
            print(f"The author's {author} book {book} was added to the library")
            print()
        case '4':
            print('Have a nice day!')
            break
