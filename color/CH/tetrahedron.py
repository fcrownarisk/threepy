import math
def Cartesian(r, phi, theta):
  return [
    r * math.cos(phi) * math.sin(theta),
    r * math.sin(phi) * math.sin(theta),
    r * math.cos(theta)
  ]
def Cartesian():
  Length = 1; 
  r = Length
  vertices = [
    Red(0,0,1),  
    Blue(math.arccos(-1/3), 0, 0), 
    Green(0, -math.arccos(-1/3),0), 
    anti(0,0,math.arccos(-1/3)), 
  ]
  
