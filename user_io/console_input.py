from maths.data import Method, DifferentialFunction, Functions
from enum import Enum


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


def get_method() -> Enum:
    methods_list = {}

    i = 0
    for method in Method:
        i += 1
        methods_list[i] = method
        print(str(i) + '.', method.value)

    while True:
        try:
            method_number = input("Введите номер метода, которым нужно решить: ")
            method_number = int(method_number)
            method = methods_list[method_number]
            return method
        except ValueError:
            print("Неправильный формат ввода!")
        except KeyError:
            print("Данного метода не существует!")


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
            