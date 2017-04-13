#zlicza ilosc dni pomiedzy dwiema datami
miesiace = {1:0,2:31,3:59,4:90,5:120,6:151,7:181,8:212,9:243,10:273,11:304,12:334}
miesiace_p = {1:0,2:31,3:60,4:91,5:121,6:152,7:182,8:213,9:244,10:274,11:305,12:335}

data1 = [13,4,2018]
data2 = [1,1,2017]
ilosc = []
lista = []
lista_dni = []

def roznica_dat(data1, data2):
    for i in range(len(data1)):
        if i == 0:
            wynik = data1[i] - data2[i]
            ilosc.append(wynik)
        elif i == 1:
            pierwszy = data1[i]
            drugi = data2[i]
            if ((data1[2] % 4 == 0 and data1[2] % 100 != 0) or data1[2] % 400 == 0) or ((data2[2] % 4 == 0 and data2[2] % 100 != 0) or data2[2] % 400 == 0):
                miesiac1 = miesiace_p[pierwszy]
                miesiac2 = miesiace_p[drugi]
            else:
                miesiac1 = miesiace[pierwszy]
                miesiac2 = miesiace[drugi]
            wynik = miesiac1 - miesiac2
            ilosc.append(wynik)
        else:
            for x in xrange(data2[i],data1[i]):
                lista.append(x)
            #print lista
            for a in lista:
                if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
                    dni = 366
                    lista_dni.append(dni)
                else:
                    dni = 365
                    lista_dni.append(dni)
            #print lista_dni
            lata_dni = sum(lista_dni)
            ilosc.append(lata_dni)

roznica_dat(data1, data2)
#print ilosc
print sum(ilosc)