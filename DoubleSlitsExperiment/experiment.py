from ClassToQuant import *

vect = np.array([[1], [0], [0], [0], [0], [0], [0], [0]])

matrix = np.array(
            [[0, 0, 0, 0, 0, 0, 0, 0], [1 / np.sqrt(2), 0, 0, 0, 0, 0, 0, 0], [1 / np.sqrt(2), 0, 0, 0, 0, 0, 0, 0],
             [0, -1 + 1j / np.sqrt(6), 0, 1, 0, 0, 0, 0], [0, -1 + 1j / np.sqrt(6), 0, 0, 1, 0, 0, 0],
             [0, -1 + 1j / np.sqrt(6), -1 + 1j / np.sqrt(6), 0, 0, 1, 0, 0],
             [0, 0, -1 + 1j / np.sqrt(6), 0, 0, 0, 1, 0], [0, 0, -1 + 1j / np.sqrt(6), 0, 0, 0, 0, 1]])

ans = multipleSlitsQuantum(matrix, vect, 2)  # 2 clicks
print(ans)


