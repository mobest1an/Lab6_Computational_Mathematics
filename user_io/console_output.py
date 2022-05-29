def output_dots(dots, real_function, method_name):
    print("\n\nРезультаты вычисления методом:", method_name)
    print("%12s%12s%12s%12s" % ("X", "Y", "Real_Y", "Delta_Y"))
    for dot in dots:
        real_y = round(real_function(dot[0]), 5)
        print("%12.4f%12.4f%12.4f%12.4f" % (round(dot[0], 5), round(dot[1], 5), real_y, round(abs(real_y - dot[1]), 5)))
