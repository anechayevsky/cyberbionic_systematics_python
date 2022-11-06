print('Welcome to our HR department!')
workers = {
    'Смирнов': {
        'посада': 'менеджер з продажу',
        'досвід роботи': 3,
        'портфоліо': 'так',
        'стек технологій': 'С++',
        'зарплата': 1000,
        'ефективність': 86
    },
    'Колягина': {
        'посада': 'менеджер з продажу',
        'досвід роботи': 3,
        'портфоліо': 'так',
        'стек технологій': 'С++',
        'зарплата': 1000,
        'ефективність': 69
    },
    'Костин': {
        'посада': 'менеджер з продажу',
        'досвід роботи': 3,
        'портфоліо': 'так',
        'стек технологій': 'С++',
        'зарплата': 1000,
        'ефективність': 78
    },
    'Щербаков': {
        'посада': 'менеджер з продажу',
        'досвід роботи': 3,
        'портфоліо': 'так',
        'стек технологій': 'С++',
        'зарплата': 1000,
        'ефективність': 91
    },
    'Борисова': {
        'посада': 'менеджер з продажу',
        'досвід роботи': 3,
        'портфоліо': 'так',
        'стек технологій': 'С++',
        'зарплата': 1000,
        'ефективність': 99
    }
}
def worker_max_efficiency(workers):
    monster_dict = {}
    for worker in workers:
        monster_dict.update({workers[worker]['ефективність']:worker})
    sorted_monsters = dict(sorted(monster_dict.items(), reverse=True))
    for key, value in sorted_monsters.items():
        print(value)

while True:
    menu = input(
        'Please select the action you wish to take: \n'
        '1. View a list of employees sorted by name \n'
        '2. Edit employee data \n'
        '3. Delete employee data \n'
        '4. Add employee data \n'
        '5. The most efficient employee is ... \n'
        '6. Finish work\n')
    match menu:
        case '1':
            sorted_workers = dict(sorted(workers.items()))
            for key, value in sorted_workers.items():
                print(key)
            print()
        case '2':
            worker = input('Please enter the last name of the employee: ')
            if worker not in workers:
                print('We do not have such an employee.')
                print()
            else:
                print(workers[worker])
                option = input("Enter the parameter you want to change (посада, досвід роботи, портфоліо, коефіцієнт ефективності, стек технологій чи зарплата) or 'break' for menu: ")
                if option not in workers[worker]:
                    print('You entered the wrong parameter.')
                    print()
                else:
                    value = input('Enter the value for the parameter: ')
                    workers[worker][option] = value
                    print(f'Employee {worker} data has been successfully edited. Updated employee data: ')
                    print(workers[worker])
                    print()
        case '3':
            worker = input('Please enter the last name of the employee for ELEMINATING!!! ')
            if worker not in workers:
                print('We do not have such an employee.')
                print()
            else:
                workers.pop(worker)
                print(f'Employee {worker} ELEMINATED successfully')
                print()
        case '4':
            worker = input('Please enter the last name of the new employee: ')
            position = input(f'Please enter position of {worker}: ')
            exp = int(input(f'Please enter work experience of {worker} (integers only, please): '))
            portfolio = input(f'Please enter portfolio existence of {worker} ("так" or "ні"): ')
            tech = input(f'Please enter technology stack of {worker}: ')
            salary = int(input(f'Please enter salary of {worker} (integers only, please): '))
            effficiency = int(input(f'Please enter efficiency ratio of {worker} (integers only, please): '))
            workers[worker] = {}
            workers[worker]['посада'] = position
            workers[worker]['досвід роботи'] = exp
            workers[worker]['стек технологій'] = tech
            workers[worker]['портфоліо'] = portfolio
            workers[worker]['зарплата'] = salary
            workers[worker]['ефективність'] = effficiency
            print(f'Data {worker} entered successfully: {workers[worker]}')
            print()
        case '6':
            print('Have a nice day!')
            break
        case '5':
            print('And the most efficient employee is ... (drumroll) ')
            worker_max_efficiency(workers)
            print()








