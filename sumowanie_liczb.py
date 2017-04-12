# Pyta o liczby dopoki suma podawanych przez uzytkownika liczb nie osiagnie lub przekroczy 100
liczby = []
while sum(liczby) < 100:
    x = input("Podaj liczbe: ")
    liczby.append(x)
print sum(liczby)