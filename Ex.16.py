# 16. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# Для n = 6: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44, 5: 2,49, 6: 2,52}


print('Привет! Я задача № 16. Я задаю список из n чисел последовательности (1+1/n)^n и вывожу их сумму')
num = int(input('Введи число n: '))
my_dict = {}
sum = 0
for i in range(1, num + 1):
    value = round((1 + 1 / i) ** i, 2)
    my_dict[i] = value
    sum += value
print(f'Сумма чисел последовательности {my_dict} равна {sum}')
print('Благодарю за внимание!')