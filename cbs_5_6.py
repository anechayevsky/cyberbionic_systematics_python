review = input('Юху! Надайте скоріше відгук та отримайте 15% знижку, якщо літер буде забагато!!!')
dirs = ['меню', 'спортзал', 'обслуговування']
for item in dirs:
    if item in review:
        print(f'Знайшов {item}!!!')
if len(review) > 60:
    print('Отримайте знижку 15% на наступне відвідування')

