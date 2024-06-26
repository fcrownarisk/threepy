import color.Red
import color.Green
import color.Blue
import color.anti
import math
def SpherePoint(t,theta,fai):
   x = 'r' * 'sin'(theta) * 'cos'(fai)
   y = 'r' * 'sin'(theta) * 'sin'(fai)
   z = 'r' * 'cos'(fai)
   T = 'r' * 'sin'(theta)
   return [x,y,z,T]
def xyz():
    x = Red
    y = Green
    z = Blue
    T = anti
    return [x,y,z,T]
def SphereRadius(x,y,z):
   {SphereRadiusx,SphereRadiusy,SphereRadiusz}
   SphereRadiusx = 'sin'(x) + 'cos'(y) + 'sin'('screenX') * 'cos'('screenY')
   SphereRadiusy = 'sin'(y) + 'cos'(x) + 'sin'('screenY') * 'cos'('screenX')
   SphereRadiusz = 'sin'(z) + 'cos'(y)
   return [SphereRadiusx,SphereRadiusy,SphereRadiusz]
def RGB():
    thisx = Red
    thisy = Green
    thisz = Red
    thist = anti
print("x,y,z,t")
