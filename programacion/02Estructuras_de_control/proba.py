dia = int(input("Introduzca su día de nacimiento: "))
mes = int(input("Introduzca su mes de nacimiento: "))
año = int(input("Introduzca su año de nacimiento: "))
suma = dia + mes + año
numsuerte = 0
for suma in range(4):
    print(suma, end=" ")
#numsuerte += int(digito)
print(numsuerte)
#print("Tu número de la suerte es", numsuerte)

# Si usamos for() con range() imprime los valores dentro del range, se utiliza para trabajar con números.
# Si usamos for() con in palabra (un valor con cadena) imprime los caracteres de la cadena 1x1, utilizado para cadenas.