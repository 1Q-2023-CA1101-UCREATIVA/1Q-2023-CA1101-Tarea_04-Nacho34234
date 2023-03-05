
import math 
x=int(input("grados Horizontales del Dardo x:"))
y=int(input("grados Verticales del Dardo y:"))
r=((math.sqrt((x)**2+(y)**2)))
def puntaje(x,y):
  return math.sqrt((x)**2+(y)**2)
resultado=puntaje(x,y)
print(resultado)
if(0 <= r <=1):
  puntos_ganados=10
  print("En el blanco ganaste ", puntos_ganados )
elif(2 <= r <= 4):
  puntos_ganados=5
  print("Cerca ganas", puntos_ganados)
elif(5 <= r <= 10):
  puntos_ganados=1
  print("lejos ganas solo", puntos_ganados )
else:
  puntos_ganados=0
  print("cayo fuera", puntos_ganados )
