# Najwiekszy Wspolny Dzielnik - Euklides

def euklides(a, b):
    while b:
        a, b = b, a % b
    return a

a = input("Podaj a: ")
b = input("Podaj b: ")
print euklides(a, b)