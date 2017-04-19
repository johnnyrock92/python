test1 = (lambda x, y: x)
test2 = (lambda x, y: y) 
jesli = (lambda b, x, y: b(x, y))

#print test1(1,2)            # 1
#print test2(1,2)            # 2
#print jesli(test1, 1, 2)    # 1
#print jesli(test2, 1, 2)    # 2

#----------------------------------------------------------------------------------------------------------

para = (lambda x, y: (lambda b: jesli(b, x, y)))
first = (lambda p: p(test1))
second = (lambda p: p(test2))

#print para(1,2)(test2)       # 2
#print first(para(1,2))       # 1
#print second(para(1,2))      # 2

#----------------------------------------------------------------------------------------------------------

zero = (lambda f, x: x)
succ = (lambda n: (lambda f, x: f(n(f, x))))
jeden = succ(zero)
dwa = succ(jeden)
trzy = succ(dwa)

f = (lambda x: x*2)
zz = 1

#print zero(f, zz)            # 1
# zero(f,zz) = zero(2,1) = (lambda 2,1: 1) = 1

#print jeden(f, zz)           # 2
# jeden(f,zz) = jeden(2,1) = succ(lambda 2, 1: 1) = succ(1) = lambda 1: (lambda 2, 1: 2(1(2,1))) =
# = lambda 1: (lambda 2, 1: 2(2,1)) = lambda 1: (lambda 2, 1: 4, 2) = lambda 1: 2 = 2

#print dwa(f, zz)             # 4
# dwa(f, zz) = dwa(2,1) = succ(2) = lambda 2: (lambda 2, 1: 2(2(2,1))) = lambda 2: (lambda 2, 1: 2(4,2)) =
# = lambda 2: (lambda 2, 1: 8, 4) = lambda 2: 4 = 4

#print trzy(f, zz)            # 8
# trzy(f,zz) = trzy(2,1) = succ(4) = lambda 4: (lambda 2, 1: 2(4(2,1))) = lambda 4: (lambda 2, 1: 2(8,4)) =
# = lambda 4: (lambda 2, 1: 16, 8) = lambda 4: 8 = 8

#----------------------------------------------------------------------------------------------------------

Z = lambda f: (lambda x: f(lambda *args: x(x)(*args)))(lambda x: f(lambda *args: x(x)(*args)))
add = Z(lambda f: lambda a, b: b if a <= 0 else 1 + f(a - 1, b))

print add(1, 1)               # 2
print add(100, 100)           # 200