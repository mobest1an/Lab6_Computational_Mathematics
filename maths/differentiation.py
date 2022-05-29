from typing import Callable


class BasicDifferentiation:
    function = None

    def __init__(self, function: Callable[[float, float], float]):
        self.function = function


class NumericalDifferentiation(BasicDifferentiation):
    y0 = None
    a = None
    b = None
    h = None
    e = None

    def __init__(self, function: Callable[[float, float], float], y0: float, a: float, b: float, h: float, e: float):
        super().__init__(function)
        self.y0 = y0
        self.a = a
        self.b = b
        self.h = h
        self.e = e

    def improved_euler_method(self) -> list:
        x_prev = self.a
        y_prev = self.y0

        dots = [[x_prev, y_prev]]

        new_h = self.h

        while True:
            x = x_prev + new_h
            y = y_prev + (new_h / 2) \
                * (self.function(x_prev, y_prev) + self.function(x, (y_prev + new_h * self.function(x_prev, y_prev))))

            y_euler = y_prev + new_h * self.function(x_prev, y_prev)

            if abs(y - y_euler) > self.e * abs(y):
                new_h /= 2
                continue

            x_prev = x
            y_prev = y

            dots.append([x, y])

            if x > self.b:
                break

        return dots

    def adams_method(self) -> list:
        n = int((self.b - self.a) / self.h)
        self.b = min(self.b, self.a + 3 * self.h)

        dots = self.improved_euler_method()

        for i in range(4, n + 1):
            df = self.function(dots[i - 1][0], dots[i - 1][1]) - self.function(dots[i - 2][0], dots[i - 2][1])

            d2f = self.function(dots[i - 1][0], dots[i - 1][1]) - 2 * self.function(dots[i - 2][0], dots[i - 2][1]) \
                  + self.function(dots[i - 3][0], dots[i - 3][1])

            d3f = self.function(dots[i - 1][0], dots[i - 1][1]) - 3 * self.function(dots[i - 2][0], dots[i - 2][1]) \
                  + 3 * self.function(dots[i - 3][0], dots[i - 3][1]) - self.function(dots[i - 4][0], dots[i - 4][1])

            x = dots[i - 1][0] + self.h
            y = dots[i - 1][1] + self.h * self.function(dots[i - 1][0], dots[i - 1][1]) \
                + (self.h ** 2) * df / 2 + 5 * (self.h ** 3) * d2f / 12 + 3 * (self.h ** 4) * d3f / 8

            dots.append([x, y])

        return dots
