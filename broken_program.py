name = input()
age = input()
year_of_birth = 2024 - age
count = 0
for year in range(year_of_birth, 2024, 2):
    print('{year} - это Ваш {count} год рождения')
    count = count + 1
print('Программа завершилась')