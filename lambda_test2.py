print (lambda x: x)(1)
print (lambda x, y: x+y)(2,4)
print (lambda x, y, z: x+y+z)(1,3,7)
print (lambda w, x,y,z: w+x+y+z)(4,6,7,3)

print (lambda x, y: x)((lambda y: y), 1)(5)
# Sposob odczytywania:
# STEP 1: print (lambda x, y: x)((lambda y: y), 1)(5)
# STEP 2: print (lambda x, y: x)(5, 1)
# STEP 3: x = 5