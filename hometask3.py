# 1. Пользователь вводит с клавиатуры номер дня недели (1-7). Необходимо вывести на
# экран названия дня недели. Например, если 1, то на экране надпись понедельник, 2 — вторник
# и т.д.

# 2. Пользователь вводит два числа. Определить, равны ли эти числа, и, если нет, вывести их
# на экран в порядке возрастания

try:
    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter second number: "))
    if num_1 == num_2:
        print("\tThe entered numbers are equal")
    elif num_1 < num_2:
        print("\tNumbers listed in ascending order:")
        print(f"\t{num_1}\n\t{num_2}")
    elif num_1 > num_2:
        print("\tNumbers listed in ascending order:")
        print(f"\t{num_2}\n\t{num_1}")
except ValueError as error:
    print(f"\tError: Please enter only int or float numbers")
except Exception as error:
    print(f"\tError: {error}")

# 3. Пользователь вводит два числа и матем действие: + - * или /
# В зависимости от введенного матем действия вывести результат