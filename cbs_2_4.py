word = input('Будь ласка, введіть фразу з клавіатури, яка складається з 10 символів: ')
result = 0
for num in range(10):
    result += ord(word[num])
print(f'Cума ASCII-кодів символів введеного рядка: {result}')