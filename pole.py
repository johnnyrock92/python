print "Program obliczajacy pole"

print "Wybierz figure"
print "1. Prostakat"
print "2. Kolo"

figura = input("> ")

if figura == 1:
    wysokosc = input("Wpisz wysokosc prostakata: ")
    szerokosc = input("Wpisz szerokosc prostokata: ")
    pole = wysokosc * szerokosc
else:
    r = input("Wpisz promien: ")
    pole = 3.14*(r**2)

print "Pole wynosi %d" % pole

