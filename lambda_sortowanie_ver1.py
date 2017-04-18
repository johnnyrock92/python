osoby = [{'nazwisko': 'Nowak', 'waga': 70, 'ulubione_dania': ['schabowy', 'pomidorowa']},
         {'nazwisko': 'Kos',   'waga': 30, 'ulubione_dania': ['lody', 'ciastka']},
         {'nazwisko': 'Szpak', 'waga': 40, 'ulubione_dania': ['ryz', 'ogorkowa']},
         {'nazwisko': 'Kowalski', 'waga': 70, 'ulubione_dania': ['schabowy', 'pomidorowa']},
         {'nazwisko': 'Konstantynopolitanczykiewicz', 'waga': 80, 'ulubione_dania': ['frytki', 'ryba']},
         ]

# Sortowanie wg nazwisk---------------------------------------------
wg_nazwisko = [nazwa['nazwisko'] for nazwa in sorted(osoby, key=lambda o: o['nazwisko'])]
print wg_nazwisko                 # ['Konstantynopolitanczykiewicz', 'Kos', 'Kowalski', 'Nowak', 'Szpak']

wg_nazwisko.sort(reverse=True)
print wg_nazwisko                 # ['Szpak', 'Nowak', 'Kowalski', 'Kos', 'Konstantynopolitanczykiewicz']


# Sortowanie wg wagi------------------------------------------------
wg_waga = [waga['waga'] for waga in sorted(osoby, key=lambda o: o['waga'])]
print wg_waga                     # [30, 40, 70, 70, 80]

wg_waga.sort(reverse=True)
print wg_waga                     # [80, 70, 70, 40, 30]

# Sortowanie wg pierwszego dania------------------------------------------------

wg_dania = [danie['ulubione_dania'][0] for danie in sorted(osoby, cmp=lambda x, y: 1 if x < y else -1, key=lambda o: o['ulubione_dania'][0])]
print sorted(wg_dania)            # ['frytki', 'lody', 'ryz', 'schabowy', 'schabowy']

wg_dania.sort(reverse=True)
print wg_dania                    # ['schabowy', 'schabowy', 'ryz', 'lody', 'frytki']