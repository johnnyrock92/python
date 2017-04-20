def function_arg(*arguments):
    print arguments

def function_keywords(**keywords):
    print keywords

def function(x,y,z):
    print x,y,z

function_arg(1,2,3,4,5,6,7,8,9)

function_keywords(a=1,b=2,c=3,d=4,e=5,f=6)

function(1,2,3)