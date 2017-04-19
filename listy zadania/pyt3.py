x = 2999

jest = True
y = 2
while (y < x) and jest:
    if (x % y) == 0:
        jest = False
    y += 1

if jest:
    print 'TAK'
else:
    print 'NIE'

# TAK