string_1 = set(input('Please, enter the first string: ').strip())
string_2 = set(input('Please, enter the second string: ').strip())
print('–°haracters that are in both strings are as follows:', *string_1.intersection(string_2))
