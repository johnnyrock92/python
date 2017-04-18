osoby = [{'nazwisko': 'Nowak', 'waga': 70, 'ulubione_dania': ['schabowy', 'pomidorowa']},
         {'nazwisko': 'Kos',   'waga': 30, 'ulubione_dania': ['lody', 'ciastka']},
         {'nazwisko': 'Szpak', 'waga': 40, 'ulubione_dania': ['ryz', 'ogorkowa']},
         {'nazwisko': 'Kowalski', 'waga': 70, 'ulubione_dania': ['schabowy', 'pomidorowa']},
         {'nazwisko': 'Konstantynopolitanczykiewicz', 'waga': 80, 'ulubione_dania': ['frytki', 'ryba']},
         ]

# Sortowanie wg nazwisk---------------------------------------------
print sorted(osoby, key=lambda o: o['nazwisko'])
print '---------------------------------------------------------------'
print sorted(osoby, key=lambda o: o['nazwisko'], reverse=True)

print '\n\n'

# Sortowanie wg wagi------------------------------------------------
print sorted(osoby, key=lambda o: o['waga'])
print '---------------------------------------------------------------'
print sorted(osoby, key=lambda o: o['waga'], reverse=True)

print '\n\n'

# Sortowanie wg pierwszego dania------------------------------------------------
print sorted(osoby, cmp=lambda x, y: 1 if x > y else -1, key=lambda o: o['ulubione_dania'][0])
print '---------------------------------------------------------------'
print sorted(osoby, cmp=lambda x, y: 1 if x < y else -1, key=lambda o: o['ulubione_dania'][0])