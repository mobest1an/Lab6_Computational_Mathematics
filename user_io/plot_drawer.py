import matplotlib.pyplot as plt


def draw_plot(dots1, dots2, real_function):
    x_ax1 = [dots[0] for dots in dots1]
    y_ax1 = [dots[1] for dots in dots1]
    x_ax2 = [dots[0] for dots in dots2]
    y_ax2 = [dots[1] for dots in dots2]

    plt.plot(x_ax1, y_ax1, "orange", linewidth=1.5, label="Усовершенствованный метод Эйлера")

    plt.plot(x_ax2, y_ax2, "red", linewidth=1.5, label="Метод Адамса")

    plt.plot(x_ax1, [real_function(elem) for elem in x_ax1], "green", linewidth=1.5, label="Точное решение")

    plt.legend()

    plt.show()
