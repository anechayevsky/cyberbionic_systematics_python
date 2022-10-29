set_1 = set(map(int, input('Enter integer values for the first list, separated by a space: ').split()))
set_2 = set(map(int, input('Enter integer values for the second list, separated by a space: ').split()))
print('Unique values of the first list: ', *set_1.difference(set_2))
print('Unique values of the second list: ', *set_2.difference(set_1))

