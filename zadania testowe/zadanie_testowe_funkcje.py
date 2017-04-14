def f(x):
    a=x
    return a+b

def g(y):
    b=f(y)
    return a+b

a = b = [1, 2]

print g(f(a))