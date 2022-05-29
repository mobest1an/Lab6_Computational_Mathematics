import matplotlib.pyplot as plt


def draw_plot(dots1, dots2):
    x_ax1 = [dots[0] for dots in dots1]
    y_ax1 = [dots[1] for dots in dots1]
    x_ax2 = [dots[0] for dots in dots2]
    y_ax2 = [dots[1] for dots in dots2]

    for x, y in dots1:
        plt.plot(x, y, 'o', color='orange')
    plt.plot(x_ax1, y_ax1, "orange", linewidth=1.5, label="Усовершенствованный метод Эйлера")

    for x, y in dots2:
        plt.plot(x, y, 'o', color='red')
    plt.plot(x_ax2, y_ax2, "red", linewidth=1.5, label="Метод Адамса")

    plt.legend()

    plt.show()
