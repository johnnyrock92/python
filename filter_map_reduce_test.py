# filter, map, reduce

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

def cube(x):
    return x*x*x

print map(cube, range(1,11))
# map wykonuje funkcje dla kazdej cyfry z zakresu


def add(x, y):
    return x+y

seq = range(10)

print map(add, seq, seq)
print map((lambda x, y: x+y), seq, seq)
# map wykonuje funkcje po kolei dla dwoch argumentow dodajac je do Siebie


# reduce----------------------------------------------------------------------
print reduce(add, range(1,11))
# reduce wykonuje funkcje po kolei liczba po liczbie
# 0+1=1, 1+2=3, 3+3=6, 6+4=10, 10+5=15, 15+6=21, 21+7=28, 28+8=36, 36+9=45, 45+10=55

def suma(seq):
    def add(x,y):
        return x+y
    return reduce(add, seq, 0)

print suma(range(1,11))