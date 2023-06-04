# 1. Пользователь вводит с клавиатуры номер дня недели (1-7). Необходимо вывести на
# экран названия дня недели. Например, если 1, то на экране надпись понедельник, 2 — вторник
# и т.д.

# 2. Пользователь вводит два числа. Определить, равны ли эти числа, и, если нет, вывести их
# на экран в порядке возрастания

# 3. Пользователь вводит два числа и матем действие: + - * или /
# В зависимости от введенного матем действия вывести результат

try:
    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter second number: "))
    math_action = input("Enter one of the available mathematical operations: + - * /: ")
    if math_action == "+":
        print("\tResult:", num_1+num_2)
    elif math_action == "-":
        print("\tResult:", num_1-num_2)
    elif math_action == "*":
        print("\tResult:", num_1*num_2)
    elif math_action == "/":
        print("\tResult:", num_1/num_2)
    else:
        raise Exception("Please choose valid mathematical operations.")
except ValueError as error:
    print("Error: Please enter correct information.")
except ZeroDivisionError as error:
    print("Error: You can't divide by zero.")
except Exception as error:
    print(f"Error: {error}.")
