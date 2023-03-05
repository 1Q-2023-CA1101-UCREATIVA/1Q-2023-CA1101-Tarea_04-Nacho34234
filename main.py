
import math 
y=int(input("grados Verticales del Dardo en y:"))
x=int(input("grados Horizontales del Dardo en x:"))
r=math.sqrt((x)**2+(y)**2)
def puntaje(x,y):
  return math.sqrt((x)**2+(y)**2)
resultado=puntaje(x,y)
print(resultado)
if(r <=1):
  print("En el blanco ganaste 10 puntos")
elif(5 <= r <= 10):
  print("Lejos ganas 1 puntos")
elif(1 <= r <= 5):
  print("Cerca ganas solo 5 punto")
else:
  print("cayo fuera 0 puntos")

