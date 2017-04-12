# Pyta o liczby dopoki suma podawanych przez uzytkownika liczb nie osiagnie 100
liczby = []
while sum(liczby) < 100:
    x = input("Podaj liczbe: ")
    liczby.append(x)
print sum(liczby)