import matplotlib.pyplot as plt
import numpy as np


def cosine(x, amplitude, angle_coefficient):
    amplitude = float(input("\nEnter the amplitude of the function:\n>>"))
    angle_coefficient = float(input("\nEnter the coefficient of the angle:\n>>"))
    y = amplitude*np.cos(angle_coefficient*(x))
    plt.plot(x, y)




def sine(x, amplitude, angle_coefficient):
    amplitude = float(input("\nEnter the amplitude of the function:\n>>"))
    angle_coefficient = float(input("\nEnter the coefficient of the angle:\n>>"))
    y = amplitude * np.sin(angle_coefficient * (x))
    plt.axis([0, 2*np.pi, -5, 5])
    plt.plot(x, y, 'b-', x, x*0, 'b--')


def tangent(x, amplitude, angle_coefficient):
    amplitude = float(input("\nEnter the amplitude of the function:\n>>"))
    angle_coefficient = float(input("\nEnter the coefficient of the angle:\n>>"))
    y = amplitude * np.tan(angle_coefficient * (x))
    plt.plot(x, y)


def linear(x, slope):
    slope = float(input("Enter the slope of the line:\n>>"))
    y = slope*x
    plt.xlim(0, 5)
    plt.ylim(0, 5)
    plt.plot(x, y)


if __name__ == "__main__":
    x = np.arange(0, 6, .01)
    xtrig = np.arange(0, 2*np.pi, .01)
    coefficient = 1
    angle_coefficient = 1

    type = input("""Enter the number of the function that you would like to graph:
    1. Linear
    2. Sine
    3. Cosine
    4. Tangent
    >> """)

    if int(type) == 1:
        linear(x, coefficient)
    elif int(type) == 2:
        sine(xtrig, coefficient, angle_coefficient)
    elif int(type) == 3:
        cosine(xtrig, coefficient, angle_coefficient)
    elif int(type) == 4:
        tangent(xtrig, coefficient, angle_coefficient)
    else:
        print("Invalid input!")

    plt.show()
