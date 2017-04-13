slownik = {0:'zero',
           1:'jeden',
           2:'dwa',
           3:'trzy',
           4:'cztery',
           5:'piec',
           6:'szesc',
           7:'siedem',
           8:'osiem',
           9:'dziewiec'
          }

def konwerter(liczba):
    liczba_rozdzielona = map(int,str(liczba))
    for i in liczba_rozdzielona:
        print slownik[i],

liczba = input('Podaj dowolna liczbe: ')
konwerter(liczba)