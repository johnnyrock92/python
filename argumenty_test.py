# test argumentow

#-------------------------------------------------------------
def test1(a, b=1, c=2):
    print "a: %s, b: %s, c: %s" % (a,b,c)

#test1(0)                   # a: 0, b: 1, c: 2
#test1(5,6)                 # a: 5, b: 6, c: 2
#test1(6, c=7)              # a: 6, b: 1, c: 7
#test1(c=0, b=-1, a=-2)     # a: -2, b: -1, c: 0
#test1(b=3, c=4)            # blad, poniewaz nie ma podanego a

#-------------------------------------------------------------
i = 1

def test2(a=i):
    print 'a =', a

i = 2

print "test2() =", test2()

# Wybierze zmienna 'i' ktora jest nad funkcja
# test2() = a = 1
# None

#-------------------------------------------------------------

def test3(a, L=[]):
    L.append(a)
    return L

print test3(1)              # [1]
print test3(2)              # [1, 2]
print test3(3)              # [1, 2, 3]

#-------------------------------------------------------------

def test4(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print test4(1)              # [1]
print test4(2)              # [2]
print test4(3)              # [3]

#-------------------------------------------------------------

def test5(x, *arguments, **keywords):
    print 'x =', x
    print '-' * 10
    print keywords
    print arguments
    keys = keywords.keys()
    keys.sort()
    for k in keys:
        print k, ':', keywords[k]

#test5(1)                       # x = 1
#test5('aaa', b='bbb', c='ccc')  
# x = aaa
# {'c': 'ccc', 'b': 'bbb'}
# ()
# b : bbb
# c : ccc

#test5(a='xxx', y='yyy', z='zzz', v='vvv') # blad, nie podano argumentu x

#-------------------------------------------------------------

def printf(format, *args):
    print format % args

printf('%s - %.3f', 'As', 123.45) # As - 123.450

print range(3, 10, 2)             # [3, 5, 7, 9]

lista = [3, 6]
print range(*lista)               # [3, 4, 5]