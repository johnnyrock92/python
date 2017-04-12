print "Program obliczajacy pole WERSJA LAMBDA"
print "\nWybierz figure"
print "1. Prostokat"
print "2. Kolo"
print "3. Kwadrat"
figura = input("> ")

pole_prostokata = lambda a, b: a*b
pole_kola = lambda pi, r: pi*r**2
pole_kwadratu = lambda a: a**2

if figura == 1:
    a = input("Podaj a: ")
    b = input("Podaj b: ")
    print pole_prostokata(a, b)
elif figura == 2:
    r = input("Podaj r: ")
    pi = 3.14
    print pole_kola(pi, r)
else:
    a = input("Podaj a: ")
    print pole_kwadratu(a)