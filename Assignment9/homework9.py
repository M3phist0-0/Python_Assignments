import numpy as np
import matplotlib.pyplot as plt


class Distributions:
    """"
    class to generate and manage different probability distros

    Attributes:
        distribution(str)= type of distribution
        mean(flot)= mean of the distribution
        std(float)= standard deviation of the distribution
        size(int)= number of samples
        data(numpy.ndarray): generated distribution data
    """
    def __init__(self, dist, mean, std, size):
        """"
        class to generate and manage different probability distros

        Args:
            dist(str)= type of distribution
            mean(flot)= mean of the distribution
            std(float)= standard deviation of the distribution
            size(int)= number of samples
        """
        self.distribution = dist.lower()
        self.mean = mean
        self.std= std
        self.size = size
        self.data = self.gen_norm_distro()

    def __str__(self):
        """"
        returns a string of the distribution details

        Returns:
            str: summary of the distro properties
        """
        return f'Distribution: {self.distribution}, Mean: {self.mean}, Standard Deviation: {self.std}, Sample SIze: {self.size}'


    def gen_norm_distro(self):
        """"
        generates the specified probability distribution

        Returns:
            numpy.ndarray: array of generated distro samples

        Raises:
            ValueError: raises error if an invalid distro type is provided
        """
        if self.distribution == 'normal':
            return np.random.normal(self.mean, self.std, self.size)

        elif self.distribution == 'lognormal':
            return np.random.lognormal(self.mean, self.std, self.size)

        elif self.distribution == 'laplace':
            return np.random.laplace(self.mean, self.std, self.size)
        else:

            raise ValueError(f'Invalid distro type {self.distribution}. Valid Types: normal, lognormal, laplace')


class NumpyDistributions:
    """"
    class to generate probability distributions using Numpy Methods

    Attributes:
        distribution(str)= type of distribution
        mean(flot)= mean of the distribution
        std(float)= standard deviation of the distribution
        size(int)= number of samples
        data(numpy.ndarray): generated distribution data
    """

    def __init__(self, dist, mean, std, size):
        """"
        initializes the NumpyDistribution class

        Args:
            dist(str)= type of distribution
            mean(flot)= mean of the distribution
            std(float)= standard deviation of the distribution
            size(int)= number of samples
        """

        self.distribution = dist.lower()
        self.mean = mean
        self.std = std
        self.size = size
        self.data = self.gen_distros()

    def gen_distros(self):
        """"
        generates the specified probability distribution using Numpy

        Returns:
            numpy.ndarray: array of generated distro samples

        Raises:
            ValueError: raises error if an invalid distro type is provided
        """

        if self.distribution == 'normal':
            return np.random.normal(self.mean, self.std, self.size)

        elif self.distribution == 'lognormal':
            return np.random.lognormal(self.mean, self.std, self.size)

        elif self.distribution == 'laplace':
            return np.random.laplace(self.mean, self.std, self.size)
        else:
            raise ValueError('Invalid Distro type: ')


    def __str__(self):
        """"
        returns a string of the distribution details

        Returns:
            str: summary of the distro properties
        """
        return f'Distribution: {self.distribution.capitalize()}, Mean: {self.mean}, Standard_Deviation: {self.std}, Sample size: {self.size}'


def plot_sin_cos_axes():
    """"
    plots sine and cosine functions on the same axes
    """
    x = np.linspace(0, 2 * np.pi, 1000)
    plt.plot(x, np.sin(x), label='Sine')
    plt.plot(x, np.cos(x), label='Cosine')
    plt.xlabel('x')
    plt.ylabel('Value')
    plt.title('Sine and Cosine on Same Axes')
    plt.legend()
    plt.grid()
    plt.show()

def plot_sin_cos_shared_y():
    """"
    plots sine and cosine functions on different axes but sharing the y-axis
    """
    x = np.linspace(0, 2 * np.pi, 1000)
    fig, ax = plt.subplots(2, 1, sharey=True)
    ax[0].plot(x, np.sin(x), label='Sine', color='blue')
    ax[0].set_title('Sine')
    ax[0].grid()
    ax[1].plot(x, np.cos(x), label='Cosine', color='orange')
    ax[1].grid()
    plt.xlabel('x')
    plt.show()

def plot_sin_cos_shared_x():
    """"
    plots the sine and cosine functions on different axes but sharing the x-axis
    """
    x = np.linspace(0, 2*np.pi, 1000)
    fig, ax = plt.subplots(1, 2, sharex=True)
    ax[0].plot(x, np.sin(x), label='Sine', color='blue')
    ax[0].set_title('Sine')
    ax[0].grid()
    ax[1].plot(x, np.cos(x), label='Cosine', color='orange')
    ax[1].set_title('Cosine')
    ax[1].grid()
    plt.ylabel('Value')
    plt.show()



if __name__ == '__main__':
    plot_sin_cos_axes()
    plot_sin_cos_shared_y()
    plot_sin_cos_shared_x()