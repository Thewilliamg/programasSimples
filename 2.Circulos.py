#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:
import math
r=round(float(input('Ingrese el radio: ')),2)
print(f"\t Perimetro: {round(2*r*math.pi,1)}\n\t Area: {round(math.pi*r**2,1)}")