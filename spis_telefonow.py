# spis telefonow
ksiazka_telefoniczna = {'Daria':512123123,
                        'Marek':600147789,
                        'Jakub':789456123
                       }
lista_imion = ['Daria', 'Marek', 'Jakub']

def spis_telefonow(ksiazka, lista):
    for imie in lista:
        print "%s: %d" % (imie, ksiazka_telefoniczna[imie])

spis_telefonow(ksiazka_telefoniczna, lista_imion)