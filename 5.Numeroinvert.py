numerostr=input("Inserte un número para encontrar el inverso:\n ")
numeroinv=""
for i in numerostr:
    numeroinv = i+numeroinv #concatena colocando primero la letra y luego el texto
print("El número invertido es {numeroinv}")