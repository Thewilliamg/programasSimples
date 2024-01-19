# Escriba un programa que pregunte al usuario
# la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:


validador=0
while validador==0: #para que al no cumplirse con el formato vuelva a iniciar el proceso
    hhmm=input("ingrese la hora actual en formato hh:mm -->")
    h=int(input("Inserte las horas -->"))
    if len(hhmm)==5 and hhmm.find(":")>0: # para verificar que se haya colocado correctamente los datos
        hh=""
        mm=""
        for i in hhmm:
            hh+=i
            mm=hhmm[hhmm.index(":")+1:len(hhmm)]
            if len(hh)==2:
                break
        hh=int(hh)
        mm=int(mm)
        horafutura=hh+h
        if horafutura>24:
            horafutura-24
        print(f" En {h} horas el reloj marcará las {horafutura}:{mm} hrs")
        validador=1
    else:
        print("----ERROR - Ingrese los datos conforme al formato hh:mm---")

