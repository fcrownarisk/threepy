import numpy as np
def inouttensor():
      inouttensor1 = np.array([[25, 10, 11, 12, 13],
                               [24, 9, 2, 3, 14],
                               [23, 8, 1, 4, 15],
                               [22, 7, 6, 5,16],
                               [21, 20, 19, 18, 17]])

      inouttensor2 = np.array([[21, 22, 23, 24,25],
                               [20, 7, 8, 9, 10],
                               [19, 6, 1, 2, 11],
                               [18, 5, 4, 3, 12],
                               [17, 16, 15, 14, 13]])

      inouttensor3 = np.array([[17, 18, 19, 20, 21],
                               [16, 5, 6, 7, 22],
                               [15, 4, 1, 8, 23],
                               [14, 3, 2, 9, 24],
                               [13, 12, 11, 10, 25]])

      inouttensor4 = np.array([[13, 14, 15, 16, 17],
                               [12, 3, 4, 5, 18],
                               [11, 2, 1, 6, 19],
                               [10, 9, 8, 7, 20],
                               [25, 24, 23, 22, 21]])
      return [inouttensor1, inouttensor2,inouttensor3,inouttensor4]
print(inouttensor)