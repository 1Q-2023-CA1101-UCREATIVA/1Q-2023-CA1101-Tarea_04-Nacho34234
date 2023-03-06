
import math 

def puntaje(x,y):
    puntaje = 0 
    r = math.sqrt(x**2 + y**2)
    if r <= 1:
      puntaje = 10
    elif r <= 5:
      puntaje = 5
    elif r <= 10:
      puntaje = 1
    else:
       puntaje=0

    return puntaje