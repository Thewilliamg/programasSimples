#   Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, 
#   y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.
import math
c1=int(input("ingrese la nota certamen 1 :"))
c2=int(input("ingrese la nota certamen 2 :"))
nl=int(input("ingrese la nota de laboratorio :"))
nc=(60-nl*0.3)/0.7
c3=3*nc-c1-c2
print(f"La nota que necesita es {math.ceil(c3)}")