from typing import Callable


def output_dots(dots: list, real_function: Callable[[float, float], float], method_name: str):
    print("\n\nРезультаты вычисления методом:", method_name)
    print("%12s%12s%12s%12s" % ("X", "Y", "Real_Y", "Delta_Y"))
    for dot in dots:
        real_y = round(real_function(dot[0]), 6)
        print("%12.6f%12.6f%12.6f%12.6f" % (round(dot[0], 6), round(dot[1], 6), real_y, round(abs(real_y - dot[1]), 6)))
