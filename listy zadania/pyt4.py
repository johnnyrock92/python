x = 1
y = 2
def f(a):
    global x
    x = a
    y = a + 1

f(4)
print x, y  # 4 2