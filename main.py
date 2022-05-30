from maths.differentiation import NumericalDifferentiation
from user_io.console_input import *
from user_io.console_output import output_dots
from user_io.plot_drawer import draw_plot

if __name__ == "__main__":
    differential_function = get_function()

    differential_function.h = get_h()
    differential_function.e = get_e()

    numerical_differentiation = NumericalDifferentiation(differential_function)

    dots1 = numerical_differentiation.improved_euler_method()
    dots2 = numerical_differentiation.adams_method()

    output_dots(dots1, differential_function.solution, "Усовершенствованный метод Эйлера")
    output_dots(dots2, differential_function.solution, "Метод Адамса")

    draw_plot(dots1, dots2, differential_function.solution)
