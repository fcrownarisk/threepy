import numpy as np

def NNtensor():
    NNtensor1 = np.array([[1, 0, 0, 1],
                          [1, 1, 0, 1],
                          [1, 0, 1, 1],
                          [1, 0, 0, 1]])
    
    NNtensor2 = np.array([[2, 0, 0, 2],
                          [2, 2, 0, 2],
                          [2, 0, 2, 2],
                          [2, 0, 0, 2]])
    
    NNtensor3 = np.array([[3, 0, 0, 3],
                          [3, 3, 0, 3],
                          [3, 0, 0, 3],
                          [3, 0, 0, 3]])
    
    NNtensor4 = np.array([[4, 0, 0, 4],
                          [4, 4, 0, 4],
                          [4, 0, 4, 4],
                          [4, 0, 4, 0]])
    
    NNtensor5 = np.array([[5, 0, 0, 5],
                          [5, 5, 0, 5],
                          [5, 0, 5, 5],
                          [5, 0, 0, 5]])
    
    NNtensor6 = np.array([[6, 0, 0, 6],
                          [6, 6, 0, 6],
                          [6, 0, 0, 6],
                          [6, 0, 0, 6]])
    
    NNtensor7 = np.array([[7, 0, 0, 7],
                          [7, 7, 0, 7],
                          [7, 0, 7, 7],
                          [7, 0, 0, 7]])
    
    NNtensor8 = np.array([[8, 0, 0, 8],
                          [8, 8, 0, 8],
                          [8, 0, 8, 8],
                          [8, 0, 0, 8]])
    
    NNtensor9 = np.array([[9, 0, 0, 9],
                          [9, 9, 0, 9],
                          [9, 0, 9, 9],
                          [9, 0, 0, 9]])
    
    return [NNtensor1, NNtensor2, NNtensor3, NNtensor4, NNtensor5, NNtensor6, NNtensor7, NNtensor8, NNtensor9]
print(NNtensor)