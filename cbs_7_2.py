links_dict = {}
while True:
    menu = input('\nSpecify what you want to do: \n'
                 '1. Assign a short link to a long link \n'
                 '2. Get the full link for the short one\n'
                 '3. Finish the job\n')
    match menu:
        case '1':
            long_link = input('Please enter the link for which you want to assign a short link: ')
            short_link = input('Please enter the short link you wish to assign: ')
            while short_link in links_dict:
                short_link = input(
                    'A short link is already assigned to another link, enter another link or print "break" for return to menu:  ')
                if short_link == 'break':
                    break
            links_dict.update({short_link: long_link})
            print(f'A short link {short_link} is assigned for the link {long_link}')
        case '2':
            short_link = input('Please enter the short link for which you want to know the full: ')
            while short_link not in links_dict:
                short_link = input(
                    'A short link is not assigned to another link, enter another link or print "break" for return to menu:  ')
                if short_link == 'break':
                    break
            print(f'A short link {short_link} is assigned for the link {long_link}')
        case '3':
            print('Have a nice day!')
            break
