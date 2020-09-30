# Numpy is a library that provides many different math utilities as well as
# a convenient datastructure to work with vectors and matrices
import numpy as np

# matplotlib allows us to draw plots
import matplotlib.pyplot as plt


def plot_tanh(x):
    # Note: Numpy functions are applied element-wise.
    y = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
    plt.plot(x, y, '--', label='tanh')


def plot_sin(x):
    y = np.sin(x)
    plt.plot(x, y, '*', label='sin')


def plot_sigmoid(x):
    y = 1 / (1 + np.exp(-x))
    plt.plot(x, y, '.',label='sigmoid')


def main():
    # We use the linspace function to define the points,
    # where we want to evaluate the function. 
    # See: https://numpy.org/doc/
    x = np.linspace(-6, 6, num=100)

    # Plot different functions
    plot_tanh(x)
    plot_sin(x)
    plot_sigmoid(x)

    # Furthermore, we can set a title to our plot
    plt.title('Plot examples')

    # We can do the same for axes
    plt.xlabel('X')
    plt.ylabel('Y')

    # Draw a legend so we can easily identify the different functions
    plt.legend()

    # Display a window to show our plot
    plt.show()


if __name__ == "__main__":
    main()
