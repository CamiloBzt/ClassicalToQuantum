# ClassicalToQuantum

This library simulates different experiments, such as:
- Marble experiment with Boolean coefficients.
- Probabilistic classic multiple slit experiment, with more than two slits.
- Quantum Multiple Slits Experiment.
- Function that graphs with a bar diagram the probabilities of a vector of states.

###Marble experiment with Boolean coefficients
```
matrix = np.array([[False, False, False, False, False, False],
                   [False, False, False, True, False, False],
                   [False, True, False, False, False, True]])
vector = np.array([[1], [0], [0])
clicks = integer
canicsBool(matrix, vect, clicks)
```
###Probabilistic classic multiple slit experiment, with more than two slits
```
matrix = np.array(
            [[0, 0, 0, 0, 0, 0],
             [1/2, 0, 0, 0, 0, 0],
             [1/2, 0, 0, 0, 0, 0],
             [0, 1/3, 0, 1, 0, 0],
             [0, 1/3, 1/3, 0, 1, 0],
             [0, 0, 1/3, 0, 0, 1]])
vect = np.array([[1], [0], [0], [0], [0], [0]])
clicks = integer
multipleSlitsProbabil(matrix, vect, clicks)
```
###Quantum Multiple Slits Experiment
```
matrix = np.array(
            [[0, 0, 0, 0, 0, 0],
             [1 / np.sqrt(2), 0, 0, 0, 0, 0],
             [1 / np.sqrt(2), 0, 0, 0, 0, 0],
             [0, -1 + 1j / np.sqrt(6), 0, 1, 0, 0],
             [0, -1 + 1j / np.sqrt(6), -1 + 1j / np.sqrt(6), 0, 0, 1, 0],
             [0, 0, -1 + 1j / np.sqrt(6), 0, 0, 0, 1]])
vect = np.array([[1], [0], [0], [0], [0], [0]])
clicks = integer
multipleSlitsQuantum(matrix, vect, clicks)
```
###Graphs
```
vect = np.array([[0.3],
                 [0.1],
                 [0.6]])
chart(vect)
```
## Getting Started

- You have to clone this library for using it in your PC.
- Then you have to move it to the folder you want.
- Cloning the library

You have to write this in your Git cmd (If you do not have Git on your computer you can install it [Here](https://git-scm.com/))
```git bash
https://github.com/CamiloBzt/ClassicalToQuantum.git
```

In this moment you will have the repository in your PC

## Prerequisites
- [Python](https://www.python.org/)
- Numpy and Matplotlib libraries


## Running the tests

For running the predetermined test you have to open the file **unitTest.py** and then just run it, then it will show you the results from the tests.

The tests are based on different activities seen during the course.

##The marble test is based on:
![](Images/marble.PNG)

![](Images/marble2.PNG)

What is the amount of marbles that will be in box 2 after 5000 clicks.
##The slits classical is based on:
###Test 1:
 ![](Images/rendijaClasica.PNG)
###Test 2:
 ![](Images/plots.PNG)

Suppose the initial state of position is given by:

Probability of being in Golden Square: 1%.

Probability of being in Soho Square: 90%.

Probability of being in St Anne's Churchyard: 9%.

And that the personality system is initially in state:

Being Dr. Jekyll: 5%

Being Mr. Hyde: 95%

What is the probability of finding Dr. Jekyll in St Anne's Churchyard after 2 clicks of time? 

##The slits quantum is based on:
###Test 1:
![](Images/rendija.PNG)

###Test 2:
![](Images/quantum.PNG)

Compute the final state of the system after 4 clicks of time. Based on your computation and after making a measurement of the system to observe the position of the particle, we will be able to find it in position 1 with a probability of:

###Plot test is based on:
![](Images/plots.PNG)

Assume that the initial state of the assembled system Position-Personality, is given by the following initial states of the constituent states:
Initial state of the system Position: The character is in Golden Square with 100% probability.
Initial state of the system Personality: The character has 80% probability of being initially Dr. Jekyll and 20% probability of being initially Mr. Hyde.


## Built With

* [Python 3.8](https://python.org/) - Python


## Authors

* **Juan Camilo Bazurto Arias** - *Systems Engineering Student* - [Linkedin](https://www.linkedin.com/in/juan-camilo-b-b65379105/) - [GitHub](https://github.com/CamiloBzt)