from collections import namedtuple

Marks = namedtuple('Marks', 'прізвище алгебра геометрія історія інформатика географія')
ivanov = Marks('Іванов', 10, 11, 12, 8, 9)
petrov = Marks('Петров',10, 11, 12, 8, 9)
shevchenko = Marks('Шевченко',10, 11, 12, 8, 9)

print('Іванов має наступні оцінки:', ivanov)
group = [ivanov, petrov, shevchenko]
print(*group, sep=', \n')
