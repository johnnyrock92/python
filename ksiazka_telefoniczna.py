# wyswietla spis ksiazki telefonicznej wg plci
ksiazka_telefoniczna = {'Daria':512123123,
                        'Marek':600147789,
                        'Jakub':789456123
                       }

def wyswietl_wg_plci(plec):
    if plec == 'k':
        for i in ksiazka_telefoniczna.keys():
            imie = map(str,str(i))
            if imie[-1] == 'a':
                print "%s: %d" % (i, ksiazka_telefoniczna[i])
    elif plec == 'm':
        for i in ksiazka_telefoniczna.keys():
            imie = map(str,str(i))
            if imie[-1] != 'a':
                print "%s: %d" % (i, ksiazka_telefoniczna[i])
    else:
        print "Nie ma takiej plci"
        plec = raw_input("Podaj plec (k lub m): ")
        wyswietl_wg_plci(plec)

plec = raw_input("Podaj plec (k lub m): ")
wyswietl_wg_plci(plec)