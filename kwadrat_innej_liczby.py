# Oblicza czy podana liczba jest kwadratem liczby calkowitej
import math

def czy_jest_kwadratem(liczba):
    y = math.sqrt(liczba)
    y_int = int(round(y))
    if y_int**2 == x:
        print "%d jest kwadratem liczby calkowitej %d" % (liczba, y_int)
    else:
        print "%d nie jest kwadratem liczby calkowitej" % liczba

x = input("Podaj liczbe: ")
czy_jest_kwadratem(x)