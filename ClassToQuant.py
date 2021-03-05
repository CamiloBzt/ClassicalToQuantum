# -*- coding: utf-8 -*-
"""
@author: Camilo Bazurto
"""

import numpy as np
import matplotlib.pyplot as plt


def canicsBool(matrix, vect, clicks=1):
    """
    This function calculates the marbles experiment
    :param matrix:  Array with boolean values
    :param vect: Vector that corresponds to the initial state of the system
    :param clicks: A non-negative integer that represents the number of time clicks to be considered.
    :return: Array
    """
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
    vect2 = vect
    for i in range(clicks):
        vect2 = np.dot(matrix, vect2)
    return vect2


def multipleSlitsProbabil(matrix, vect, clicks=1):
    """
    This function calculates the probabilities of a probabilistic system
    :param matrix: Array
    :param vect: Array
    :param clicks: Int
    :return: Array
    """
    vect2 = vect
    for i in range(clicks):
        vect2 = np.dot(matrix, vect2)
    return vect2


def multipleSlitsQuantum(matrix, vect, clicks=1):
    """
    This function calculates n clicks in a quantum system
    :param matrix: Array
    :param vect: Array
    :param clicks: int
    :return: Array
    """

    vect2 = vect
    for i in range(clicks):
        vect2 = np.dot(matrix, vect2)

    for i in range(len(vect2)):
        vect2[i][0] = abs(vect2[i][0])**2
    return vect2


def chart(vect):
    """
    This function graph a status vector
    :param vect: Array
    """
    probabils = [i for i in range(len(vect))]
    bars = [vect[i][j] for i in range(len(vect)) for j in range(len(vect[i]))]
    plt.bar(probabils, bars, color="green", linewidth=3)
    plt.title('Graph')
    plt.xlabel('Condition')
    plt.ylabel('Probabilities')
    plt.grid()
    plt.savefig('plot.jpg')
    plt.show()