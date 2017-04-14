"""
x, y, z = [0], [1], [2]
x, y, z = x+y+z, x+y+z, x+y+z
print x, y, z
"""
"""
x = (y, z) = ([a], [b, c]) = ([3], [2,1])
print x, y, z, a, b, c
"""
"""
x, y, z = 3, 2, 1
x = x+y+z
y = x+y+z
z = x+y+z

print x, y, z
"""

print map(lambda x, y: x + y, range(7), range(7))