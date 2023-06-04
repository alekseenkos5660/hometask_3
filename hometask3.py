# 1. Пользователь вводит с клавиатуры номер дня недели (1-7). Необходимо вывести на
# экран названия дня недели. Например, если 1, то на экране надпись понедельник, 2 — вторник
# и т.д.

try:
    week_day = int(input("Enter the number of the day of the week: "))
    if week_day == 1:
        print("\tYou have chosen the first day of the week and it is Monday")
    elif week_day == 2:
        print("\tYou have chosen the second day of the week and it is Tuesday")
    elif week_day == 3:
        print("\tYou have chosen the third day of the week and it is Wednesday")
    elif week_day == 4:
        print("\tYou have chosen the fourth day of the week and it is Tuesday")
    elif week_day == 5:
        print("\tYou have chosen the fifth day of the week and it is Friday")
    elif week_day == 6:
        print("\tYou have chosen the sixth day of the week and it is Saturday")
    elif week_day == 7:
        print("\tYou have chosen the seventh day of the week and it is Sunday")
    else:
        raise Exception("\tPlease select a number from 1 to 7")
except ValueError as error:
    print("\tEnter only integer numbers please!")
except Exception as error:
    print(f"\tError: {error}")

# 2. Пользователь вводит два числа. Определить, равны ли эти числа, и, если нет, вывести их
# на экран в порядке возрастания

# 3. Пользователь вводит два числа и матем действие: + - * или /
# В зависимости от введенного матем действия вывести результат
