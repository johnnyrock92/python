# Sumuje 10 liczb podanych przez uzytkownika
liczby = []
while len(liczby) < 10:
    x = input("Podaj liczbe: ")
    liczby.append(x)
print sum(liczby)