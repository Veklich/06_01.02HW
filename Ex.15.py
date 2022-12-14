# 15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def ex15(num: int) -> list:
    """
    Принимает на вход число N и выдает набор произведений чисел от 1 до N
    :param num: вводит пользователь
    :return: набор произведений чисел от 1 до N. Пример: N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
    """
    my_list = [1]
    for i in range(2, num + 1):
        my_list.append(my_list[i - 2] * i)
    return my_list


print('Привет! Я задача № 15. Я могу вывести набор произведений чисел от 1 до N. Хочешь покажу?')
num = int(input('Введи число N: '))
print(f'Вуаля: {ex15(num)}')
