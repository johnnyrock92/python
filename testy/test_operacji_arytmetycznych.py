# operacje arytmetyczne na zwyklych liczbach calkowitych
# INT
x = 3
y = 2

# LONG
#x = 1000L
#y = 400L

#FLOAT
#x = 3.333
#y = 1.234

#COMPLEX
#x = 3+2j
#y = 2+1j
print '----------'
print "x = %d" % x
print "y = %d" % y
print '----------'
print "x + y =", x + y
print "x - y =", x - y 
print "x * y =", x * y 
print "x / y =", x / y   # dzielenie calkowite
print "x // y =", x // y  # zaokraglenie w dol dzielenia calkowitego
        # 3/0.7  3//0.7

print "x % y =", x % y   # reszta z dzielenia
print "-x =", -x
print "+x =", +x
print "abs(x) =", abs(x)  # wartosc bezwzgledna
print "int(x) =", int(x)  # konwersja do int
print "long(x) =", long(x) 
print "float(x) =", float(x)
c = complex(x,y) 
print "c.conjugate() =", c.conjugate()   # sprzezona do danej zespolonej  
print "divmod(x, y) =", divmod(x, y)    # para (x // y, x % y) 
print "pow(x, y) =", pow(x, y)       # x do potegi y
print "x ** y =", x ** y          # x do potegi y

