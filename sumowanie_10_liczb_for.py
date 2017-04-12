# Sumuje 10 liczb podanych przez uzytkownika
liczby = []
for i in range(10):
    x = input("Podaj liczbe: ")
    liczby.append(x)
print sum(liczby)