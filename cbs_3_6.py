work = ("понеділок", "вівторок", "середа", "четвер", "п'ятниця")
end = ('субота', 'неділя')
today = input('Який сьогодні день? ')
if today in work:
    print('Сьогодні на роботу')
elif today in end:
    print('Сьогодні вихідний')
else:
    print('Такого дня нема')