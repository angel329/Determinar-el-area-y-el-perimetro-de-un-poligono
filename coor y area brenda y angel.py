from os import system
import csv
import math

system("clear")
x = []
y = []
n=sum1=sum2=0
with open('C:\\Users\\afel0\\OneDrive\\Escritorio\\Determinar el area y el perimetro de un poligono\\coor.csv', 'r') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
            #print(row['easting'], row{'northing'])
            x.append (float(row['Easting']))
            y.append(float(row['Northing']))
            n=n+1
print ("co}ordenadas x,y (archivo coor.dat)")
for i in range(n-1):
      sum1=x[i]*y[i+1]+sum1
      sum2=y[i]*x[i+1]+sum2

sum1=x[n-1]*y[1]
sum2=y[n-1]*x[1]

print (sum1,sum2)
      
#Algoritmo para la determinación del área
sub_area = ((x[1]*y[n-1])-(x[n-1]*y[0]))*(-1)
area = sub_area/2
print (x, y, "\narea = %.2f" % area)
#Ingresar coordanadas
N = int(input("Ingresar el número de vértices: "))
for i in range(0,N):
     xP1 = int(input("Favor de ingresar la abscisa del primer punto: "))
     yP1 = int(input("Favor de ingresar la ordenada del primer punto: "))
     xP2 = int(input("Favor de ingresar la abscisa del segundo punto: "))
     yP2 = int(input("Favor de ingresar la abscisa del segundo punto: "))
     print("La distancia entre los 2 puntos es de : ",math.sqrt(abs(((xP2-xP1)*(xP2-xP1)+((yP2-yP1)*(yP2-yP1))))))
#Determinar el perimetro
Suma=math.sqrt(abs(((xP2-xP1)*(xP2-xP1)+((yP2-yP1)*(yP2-yP1)))+(N))) 
perimetro=Suma
print ('El perímetro es: ',perimetro)

