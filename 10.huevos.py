
#   Escriba un programa que reciba como entrada la temperatura original del huevo y
#   muestre como salida el tiempo en segundos que le toma alcanzar la temperatura máxima para prepararlo a la copa.
#   El tiempo en segundos que toma al centro de la yema alcanzar Ty°C está dado por la fórmula:
To=int(input("ingrese la temperatura original huevo: "))
Ty=70
Tw=100
K=0.0054
C=3.7
P=1.038
M=47
import math
t=math.pow(M,(2/3))*(C*P**(1/3))/(K*math.pi**2*(4*math.pi/3)**(2/3))*math.log(0.76*((To-Tw)/(Ty-Tw)))
#print(f"El tiempo que tarda es {round(t,2)} segundos")
print(f"El tiempo que tarda es {int(t//60)} minutos con {math.ceil(t%60)} segundos")