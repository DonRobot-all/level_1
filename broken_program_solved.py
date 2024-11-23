name = input()
age = int(input())
year_of_birth = 2024 - age
count = 1
for year in range(year_of_birth, 2024):
    print(f'{year} - это Ваш {count} год рождения')
    count = count + 1
print('Программа завершилась')