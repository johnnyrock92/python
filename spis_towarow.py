slownik = {'chleb':2,
           'cukier':3,
           'maka':1.5,
           'sol':1,
           'ziemniaki':1.7
          }

lista_towarow = ['chleb', 'cukier', 'maka', 'sol']

def spis_towarow(spis):
    for i in spis:
        print "%s: %dzl" % (i, slownik[i])

spis_towarow(lista_towarow)