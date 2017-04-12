print "Program obliczajacy pole WERSJA LAMBDA"

print "Wybierz figure"
print "1. Prostokat"
print "2. Kolo"

figura = input("> ")

if figura == 1:
    a = input("Podaj a: ")
    b = input("Podaj b: ")
    pole = lambda a, b: a*b
    print pole(a, b)
else:
    r = input("Podaj r: ")
    pi = 3.14
    pole = lambda pi, r: pi*r**2
    print pole(pi, r)