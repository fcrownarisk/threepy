import numpy as np


def outintensor():
    outintensor1 = np.array([[1, 2, 3, 4, 5],
                             [16, 17, 18, 19, 6],
                             [15, 24, 25, 20, 7],
                             [14, 23, 22, 21, 8],
                             [13, 12, 11, 10, 9]])

    outintensor2 = np.array([[13, 14, 15, 16, 1],
                             [12, 23, 24, 17, 2],
                             [11, 22, 25, 18, 3],
                             [10, 21, 20, 19, 4],
                                 [9, 8, 7, 6, 5]])
    outintensor3 = np.array([[9, 10, 11, 12, 13],
                             [8, 21, 22, 23, 14],
                             [7, 20, 25, 24, 15],
                             [6, 19, 18, 17, 16],
                             [5, 4, 3, 2, 1]])

    outintensor4 = np.array([[5, 6, 7, 8, 9],
                             [4, 19, 20, 21, 10],
                             [3, 18, 25, 22, 11],
                             [2, 17, 24, 23, 12],
                             [1, 16, 15, 14, 13]])

    return [outintensor1, outintensor2, outintensor3, outintensor4]
print(outintensor)