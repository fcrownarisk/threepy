import sphere
import color.Red
import color.Green
import color.Blue
import anti
import math
import numpy as np
def Cylinder(X,Y,Z):
     CylinderXY = 'Cylinder.X+ Cylinder.Y'
     CylinderYZ = 'Cylinder.Y+ Cylinder.Z'
     CylinderZX = 'Cylinder.Z + Cylinder.X'
     CylinderXYZ = 'Cylinder.X + Cylinder.Y + Cylinder.Z'
     return [CylinderXY,CylinderYZ,CylinderZX,CylinderXYZ,X,Y,Z]

def CylindetXY():
    element1 = np.array
    ([[0][1][0][1],
      [1][0][1][0],
      [0][0][0][1],
      [0][0][0][0]])
    element2 = np.array
    ([[0][1][0][1],
      [0][0][1][0],
      [0][1][0][1],
      [0][0][0][0]])
    element3 = np.array
    ([[0][1][0][1],
      [0][0][1][0],
      [0][0][0][1],
      [0][0][1][0]])
    element4 = np.array
    ([[0][1][0][1],
      [0][0][1][0],
      [0][0][0][1],
      [1][0][0][0]])
    return [element1,element2,element3,element4]
def CylinderYZ():
    element5 = np.array
    ([[1][0][1][0],
      [0][1][0][0],
      [0][0][1][0],
      [0][0][0][1]])

    element6 = np.array
    ([[1][0][0][0],
      [0][1][0][1],
      [0][0][1][0],
      [0][0][0][1]])

    element7 = np.array
    ([[1][0][0][0],
      [0][1][0][0],
      [0][0][1][0],
      [0][1][0][1]])

    element8 = np.array
    ([[1][0][0][0],
      [0][1][0][0],
      [1][0][1][0],
      [0][0][0][1]])
    return [element5,element6,element7,element8]
def CylinderXZ():
    element9 = np.array
    ([[0][1][0][1],
      [1][0][1][0],
      [0][0][0][1],
      [0][0][0][0]])
 
    element10 = np.array
    ([[0][1][0][1],
      [0][0][1][0],
      [0][1][0][1],
      [0][0][0][0]])

    element11 = np.array
    ([[0][1][0][1],
      [0][0][1][0],
      [0][0][0][1],
      [0][0][1][0]])
 
    element12 = np.array
    ([[0][1][0][1],
      [0][0][1][0],
      [0][0][0][1],
      [1][0][0][0]])
    return[element9, element10, element11, element12]

def CylinderXYZ():
    element13 = np.array
    ([[1][0][1][0],
      [0][0][0][1],
      [1][0][0][0],
      [0][1][0][0]])
 
    element14 = np.array
    ([[0][0][1][0],
      [0][1][0][1],
      [1][0][0][0],
      [0][1][0][0]])
 
    element15 = np.array
    ([[0][0][1][0],
      [0][0][0][1],
      [1][0][1][0],
      [0][1][0][0]])

    element16 = np.array
    ([[0][0][1][0],
      [0][0][0][1],
      [1][0][0][0],
      [0][1][0][1]])

    element17 = np.array
    ([[0][1][0][0],
      [1][0][0][0],
      [0][1][0][0],
      [1][0][1][0]])

    element18 = np.array
    ([[0][0][0][0],
      [1][0][1][0],
      [0][1][0][0],
      [1][0][1][0]])

    element19 = np.array
    ([[0][0][0][0],
      [1][0][0][0],
      [0][1][0][1],
      [0][0][1][0]])

    element20 = np.array
    ([[0][0][0][1],
      [1][0][0][0],
      [0][1][0][0],
      [0][0][1][0]])
