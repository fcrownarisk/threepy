import numpy as np
def antiinouttensor():

    antioutintensor1 = np.array([[1, 16, 15, 14, 13],
                                 [2, 17, 24, 23, 12],
                                 [3, 18, 25, 22, 11],
                                 [4, 19, 20, 21, 10],
                                 [5, 6, 7, 8, 9]])

    antioutintensor2 = np.array([[13, 12, 11, 10, 9],
                                 [14, 23, 22, 21, 8],
                                 [15, 24, 25, 20, 7],
                                 [16, 17, 18, 19, 6],
                                 [1, 2, 3, 4, 5]])
    antioutintensor3 = np.array([[9, 8, 7, 6, 5],
                                 [10, 21, 20, 19, 4],
                                 [11, 22, 25, 18, 3],
                                 [12, 23, 24, 17, 2],
                                 [13, 14, 15, 16, 1]])

    antioutintensor4 = np.array([[5, 4, 3, 2, 1],
                                 [6, 19, 18, 17, 16],
                                 [7, 20, 25, 24, 15],
                                 [8, 21, 22, 23, 14],
                                 [9, 10, 11, 12, 13]])
    return [antioutintensor1,antioutintensor2,antioutintensor3,antioutintensor4]
print(antiinouttensor)