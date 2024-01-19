#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:
n=int(input("Ingrese la CANTIDAD de notas a la que desea calcular el promedio: "))
notas=[]
acumulado=0
for i in range(n):
    notas.append(float(input(f"Ingrese la nota {i+1}: ")))
    acumulado+=notas[i]
print(f"El promedio es {round(acumulado/n,2)}")    
