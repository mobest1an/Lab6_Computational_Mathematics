from maths.data import BasicFunction, DifferentialFunction


class BasicDifferentiation:
    function = None

    def __init__(self, function: BasicFunction):
        self.function = function


class NumericalDifferentiation(BasicDifferentiation):
    y0 = None
    a = None
    b = None
    h = None
    e = None

    def __init__(self, differential_function: DifferentialFunction):
        super().__init__(differential_function)
        self.function = differential_function

    def improved_euler_method(self) -> list:
        x_prev = self.function.a
        y_prev = self.function.y0

        dots = [[x_prev, y_prev]]

        new_h = self.function.h

        calculate_y = lambda x, y, h, f: y + h / 2 * (f(x, y) + f(x + h, (y + h * f(x, y))))

        while True:
            x = x_prev + new_h
            y = calculate_y(x_prev, y_prev, new_h, self.function.function)

            y_half_h = calculate_y(x_prev + new_h, calculate_y(x_prev, y_prev, new_h / 2, self.function.function), new_h / 2, self.function.function)

            if abs(y - y_half_h) > self.function.e:
                new_h /= 2
                continue

            x_prev = x
            y_prev = y

            dots.append([x, y])

            if round(x, 6) > round(self.function.b, 6):
                break

        dots.pop(-1)

        return dots

    def adams_method(self) -> list:
        old_b = self.function.b
        self.function.b = min(self.function.b, self.function.a + 3 * self.function.h)

        dots = self.improved_euler_method()

        for i in range(len(dots), 999999999):
            df = self.function.function(dots[i - 1][0], dots[i - 1][1]) - self.function.function(dots[i - 2][0], dots[i - 2][1])

            d2f = self.function.function(dots[i - 1][0], dots[i - 1][1]) - 2 * self.function.function(dots[i - 2][0], dots[i - 2][1]) \
                  + self.function.function(dots[i - 3][0], dots[i - 3][1])

            d3f = self.function.function(dots[i - 1][0], dots[i - 1][1]) - 3 * self.function.function(dots[i - 2][0], dots[i - 2][1]) \
                  + 3 * self.function.function(dots[i - 3][0], dots[i - 3][1]) - self.function.function(dots[i - 4][0], dots[i - 4][1])

            x = dots[i - 1][0] + self.function.h
            y = dots[i - 1][1] + self.function.h * self.function.function(dots[i - 1][0], dots[i - 1][1]) \
                + (self.function.h ** 2) * df / 2 + 5 * (self.function.h ** 3) * d2f / 12 + 3 * (self.function.h ** 4) * d3f / 8

            dots.append([x, y])

            if round(x, 6) > round(old_b, 6):
                break

        dots.pop(-1)

        return dots
