a = 2018
b = 2016
lista = []
lista_dni = []
while a >= b:
    lista.append(b)
    b+=1
print lista

for i in lista:
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        dni = 366
        lista_dni.append(dni)
    else:
        dni = 365
        lista_dni.append(dni)

print lista_dni
print sum(lista_dni)