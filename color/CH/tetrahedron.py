import math
def Cartesian(r, phi, theta):
  return [
    r * 'cos'(phi) * 'sin'(theta),
    r * 'sin'(phi) * 'sin'(theta),
    r * 'cos'(theta)
  ]
def Cartesian():
  Length = 1; 
  r = Length
  vertices = [
    'Red'(0,0,1),  
    'Blue'('cos'(-1/3), 0, 0), 
    'Green'(0, -'cos'(-1/3),0), 
    'anti'(0,0,'cos'(-1/3)), 
  ]
  