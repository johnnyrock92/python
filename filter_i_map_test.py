# filter, map

# filter-------------------------------------------------------------------
def funkcja(x):
    return x % 2 == 0

print filter(funkcja, range(2, 13))
# filter wykonuje funkcje dla kazdej liczby z zakresu
# gdy cyfra z podanego zakresu jest parzysta to zwroci te cyfre



# map-----------------------------------------------------------------------
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print map(funkcja, lista)
# map wykonuje funkcje po kolei dla kazdego elementu listy zwracajac liste True lub False
# gdy parzysta zwroci TRUE, gdy nieparzysta zwroci FALSE
