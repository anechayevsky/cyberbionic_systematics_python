string_1 = set(input('Please, enter the first string: ').strip())
string_2 = set(input('Please, enter the second string: ').strip())
inter = string_1.intersection(string_2)
print('Сharacters that are in both strings are as follows:', *inter)
