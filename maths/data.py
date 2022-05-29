from typing import Callable
from enum import Enum
import numpy as np


class BasicFunction:
    function = None
    presentation = None

    def __init__(self, function: Callable[[float, float], float], presentation: str):
        self.function = function
        self.presentation = presentation


class DifferentialFunction(BasicFunction):
    solution = None
    y0 = None
    a = None
    b = None
    h = None
    e = None

    def __init__(self, function: Callable[[float, float], float], presentation: str, solution: Callable[[float], float],
                 y0: float, a: float, b: float, h: float = None, e: float = None):
        super().__init__(function, presentation)
        self.solution = solution
        self.y0 = y0
        self.a = a
        self.b = b
        self.h = h
        self.e = e


class Functions(Enum):
    FIRST = DifferentialFunction(lambda x, y: x ** 3 - y, "y' = x^3 - y на [0; 2] при y(0) = 0",
                                 lambda x: x ** 3 - 3 * x ** 2 + 6 * x + 6 * np.exp(-x) - 6, 0, 0, 2)
    SECOND = DifferentialFunction(lambda x, y: y + (1 + x) * y ** 2, "y' = y + (1 + x) * y^2 на [1; 1.5] при y(1) = -1",
                                  lambda x: - 1 / x, -1, 1, 1.5)
    THIRD = DifferentialFunction(lambda x, y: x + 1 - y, "y' = x + 1 - y на [1; 1.6] при y(1) = 2",
                                 lambda x: np.exp(1 - x) + x, 2, 1, 1.6)


class Method(Enum):
    IMPROVED_EULER = 'Усовершенствованный метод Эйлера'
    ADAMS = 'Метод Адамса'
