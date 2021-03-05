import unittest
import numpy as np
import ClassToQuant as ctq


class TestClassToQuan(unittest.TestCase):

    def testCanic(self):
        matrix = np.array([[False, False, False, False, False, False], [False, False, False, True, False, False],
                           [False, True, False, False, False, True], [False, False, True, False, False, False],
                           [False, False, False, False, True, False], [True, False, False, False, False, False]])
        vect = np.array([[6], [0], [3], [5], [3], [8]])
        clicks = 2
        ans = ctq.canicsBool(matrix, vect, clicks)
        self.assertEqual(ans[2][0], 11)

    def testSlitsProbabil(self):
        # Test 1
        matrix = np.array([[0, 1 / 6, 5 / 6], [1 / 3, 1 / 2, 1 / 6], [2 / 3, 1 / 3, 0]])
        state = np.array([[1 / 3, 2 / 3], [2 / 3, 1 / 3]])
        system = np.kron(matrix, state)
        vect1 = np.array([[0.01], [0.9], [0.09]])
        vect2 = np.array([[0.05], [0.95]])
        state2 = np.kron(vect1, vect2)
        ans = ctq.multipleSlitsProbabil(system, state2, 2)
        # What is the probability of finding Dr. Jekyll in St Anne's Churchyard after 2 clicks of time?
        self.assertEqual(round(ans[4][0] * 100, 2), 13.77)

        # Test 2
        matrix = np.array(
            [[0, 0, 0, 0, 0, 0, 0, 0], [1 / 2, 0, 0, 0, 0, 0, 0, 0], [1 / 2, 0, 0, 0, 0, 0, 0, 0],
             [0, 1 / 3, 0, 1, 0, 0, 0, 0],
             [0, 1 / 3, 0, 0, 1, 0, 0, 0], [0, 1 / 3, 1 / 3, 0, 0, 1, 0, 0], [0, 0, 1 / 3, 0, 0, 0, 1, 0],
             [0, 0, 1 / 3, 0, 0, 0, 0, 1]])
        vect = np.array([[1], [0], [0], [0], [0], [0], [0], [0]])
        ans = ctq.multipleSlitsProbabil(matrix, vect, 2)  # 2 clicks
        # What is the probability on the fifth target?
        self.assertEqual(ans[5], [1 / 3])

    def test_cuan(self):
        # Test 1
        matrix = np.array(
            [[0, 0, 0, 0, 0, 0, 0, 0], [1 / np.sqrt(2), 0, 0, 0, 0, 0, 0, 0], [1 / np.sqrt(2), 0, 0, 0, 0, 0, 0, 0],
             [0, -1 + 1j / np.sqrt(6), 0, 1, 0, 0, 0, 0], [0, -1 + 1j / np.sqrt(6), 0, 0, 1, 0, 0, 0],
             [0, -1 + 1j / np.sqrt(6), -1 + 1j / np.sqrt(6), 0, 0, 1, 0, 0],
             [0, 0, -1 + 1j / np.sqrt(6), 0, 0, 0, 1, 0], [0, 0, -1 + 1j / np.sqrt(6), 0, 0, 0, 0, 1]])
        vect = np.array([[1], [0], [0], [0], [0], [0], [0], [0]])
        ans = ctq.multipleSlitsQuantum(matrix, vect, 2)  # 2 clicks
        # What is the probability on the fifth target?
        self.assertEqual(round(ans[5][0].real, 3), 2.333)
        # Test 2
        matrix = np.array([[1 / np.sqrt(2), 1 / np.sqrt(2), 0], [-1j / np.sqrt(2), 1j / np.sqrt(2), 0], [0, 0, -1j]])
        vect = np.array([[1 / np.sqrt(3)], [2j / np.sqrt(15)], [np.sqrt(2 / 5)]])
        ans = ctq.multipleSlitsQuantum(matrix, vect, 4)  # 4 clicks
        # Compute the final state of the system after 4 clicks of time. Based on your computation and after making a
        # measurement of the system to observe the position of the particle, we will be able to find it in position 1
        # with a probability of:
        self.assertEqual(round(ans[1][0].real*100, 2), 30)

    def testPlot(self):
        matrix = np.array([[0, 1 / 6, 5 / 6], [1 / 3, 1 / 2, 1 / 6], [2 / 3, 1 / 3, 0]])
        state = np.array([[1 / 3, 2 / 3], [2 / 3, 1 / 3]])
        system = np.kron(matrix, state)
        vect1 = np.array([[1], [0], [0]])
        vect2 = np.array([[0.8], [0.2]])
        state2 = np.kron(vect1, vect2)
        asn = ctq.multipleSlitsProbabil(system, state2)  # 1 Click
        ctq.chart(asn)


if __name__ == '__main__':
    unittest.main()
