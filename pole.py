print "Program obliczajacy pole"
print "\nWybierz figure"
print "1. Prostokat"
print "2. Kolo"
print "3. Kwadrat"
figura = input("> ")

if figura == 1:
    a = input("Podaj a: ")
    b = input("Podaj b: ")
    pole = a * b
elif figura == 2:
    r = input("Podaj r: ")
    pole = 3.14*(r**2)
else:
    a = input("Podaj a: ")
    pole = a**2

print "Pole wynosi %d" % pole