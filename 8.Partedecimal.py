#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.
num=input("Igrese un numero real con parte decimal ")
decimal=float(num[num.find("."):len(num)])
print(decimal)
