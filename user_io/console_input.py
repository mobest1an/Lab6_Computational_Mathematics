from maths.data import DifferentialFunction, Functions


def get_function() -> DifferentialFunction:
    functions_list = {}

    i = 0
    for function in Functions:
        i += 1
        functions_list[i] = function.value
        print(str(i) + '.', function.value.presentation)

    while True:
        try:
            function_number = input("Выберите номер функции: ")
            if function_number == "":
                return functions_list[1]
            function_number = int(function_number)
            function = functions_list[function_number]
            break
        except ValueError:
            print("Неправильный формат ввода!")
        except KeyError:
            print("Данной функции не существует!")

    return function


def get_h() -> float:
    while True:
        try:
            h = float(input("Введите шаг: "))
            return h
        except ValueError:
            print("Неправильный формат ввода!")


def get_e() -> float:
    while True:
        try:
            e = float(input("Введите точность: "))
            return e
        except ValueError:
            print("Неправильный формат ввода!")
