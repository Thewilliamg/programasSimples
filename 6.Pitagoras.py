#Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b
# de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c
# del triangulo, dado por el teorema de Pitágoras: c2=a2+b2
print("Hay un triangulo rectangulo de catetos 'a' y 'b'")
a=int(input("Ingrese cateto a: "))
b=int(input("Ingrese cateto b: "))
print(f"La hipotenusa es {(a**2+b**2)**0.5}")