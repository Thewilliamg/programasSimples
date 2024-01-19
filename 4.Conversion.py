#Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.
cm=float(input("Ingrese longitud en centimetros :"))
inches=round(cm/2.54,2)
print(f"{cm} cm = {inches} inches")