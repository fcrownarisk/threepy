import numpy as np
def antiinouttensor():

    antinoutensor1 = np.array([[13, 12, 11, 10, 25],
                               [14, 3, 2, 9, 24],
                               [15, 4, 1, 8, 23],
                               [16, 5, 6, 7, 22],
                               [17, 18, 19, 20, 21]])

    antinoutensor2 = np.array([[25, 24, 23, 22, 21],
                               [10, 9, 8, 7, 20],
                               [11, 2, 1, 6, 19],
                               [12, 3, 4, 5, 18],
                               [13, 14, 15, 16, 17]])

    antinoutensor3 = np.array([[21, 20, 19, 18, 17],
                               [22, 7, 6, 5, 16],
                               [23, 8, 1, 4, 15],
                               [24, 9, 2, 3, 14],
                               [25, 10, 11, 12, 13]])

    antinoutensor4 = np.array([[17, 16, 15, 14, 13],
                               [18, 5, 4, 3, 12],
                               [19, 6, 1, 2, 11],
                               [20, 7, 8, 9, 10],
                               [21, 22, 23, 24, 25]])
    return [antinoutensor1,antinoutensor2,antinoutensor3,antinoutensor4]
print(antiinouttensor)