dia = int(input("Introduzca su día de nacimiento: "))
mes = int(input("Introduzca su mes de nacimiento: "))
año = int(input("Introduzca su año de nacimiento: "))
suma = dia + mes + año
numsuerte = 0
suma = str(suma)
for digito in suma:
    numsuerte += int(digito)
print("Tu número de la suerte es", numsuerte)