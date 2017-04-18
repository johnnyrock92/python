test1 = (lambda x: (lambda y: x))
test2 = (lambda x: (lambda y: y))
jesli = (lambda b: (lambda x: (lambda y: (b(x))(y))))

print ((jesli(test1))(1))(2)
print ((jesli(test2))(1))(2)

print ((jesli(test1))(3))(4)
print ((jesli(test2))(3))(4)