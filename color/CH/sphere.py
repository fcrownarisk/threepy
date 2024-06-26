import color.Red
import color.Green
import color.Blue
import color.anti
import math
def SpherePoint(t,theta,fai):
   x = r * math.sin(theta) * math.cos(fai)
   y = r * math.sin(theta) * math.sin(fai)
   z = r * math.cos(fai)
   T = r * math.sin(theta)
   return [x,y,z,T]
def xyz():
    x = Red
    y = Green
    z = Blue
    T = anti
    return [x,y,z,T]
def SphereRadius(x,y,z):
   {SphereRadiusx,SphereRadiusy,SphereRadiusz}
   SphereRadiusx = math.sin(x) + math.cos(y) + math.sin(screenX) * math.cos(screenY)
   SphereRadiusy = math.sin(y) + math.cos(x) + math.sin(screenY) * math.cos(screenX)
   SphereRadiusz = math.sin(z) + math.cos(y)
   return [SphereRadiusx,SphereRadiusy,SphereRadiusz]
def RGB():
    this.x = Red
    this.y = Green
    this.z = Red
    this.t = anti
print("x,y,z,t")
