# test operatorow AND i OR
print "---------------------------------------------------------------------"
# AND - gdy wszystkie wartosci sa prawda zwroci ostatnia prawde
print "a and b =", 'a' and 'b'
# OR - gdy wszystkie wartosci sa prawda zwroci pierwsza prawde
print "a or b =", 'a' or 'b'
print "---------------------------------------------------------------------"
# 0, '', [], {}, None - sa falszem
# 1, litery - sa prawda
# AND - gdy ktoras z wartosci jest falszem to zwraca pierwszy napotkany falsz
print "'' and b =", '' and 'b'

# OR - gdy ktoras z wartosci jest prawda to zwraca pierwsza napotkana prawde
print "'' or b =", '' or 'b'
print "---------------------------------------------------------------------"

print "a and b and c =", 'a' and 'b' and 'c' # zwroci ostatnia prawde
print "a or b or c =", 'a' or 'b' or 'c' # zwroci pierwsza prawde
print "'' and [] and {} =", '' and [] and {} # zwroci pierwszy falsz
print "'' or [] or {} =", '' or [] or {} # zwroci ostatni falsz
print "---------------------------------------------------------------------"

def funkcja():
    print "funkcja()",
    return 1

print "a and funkcja() = ", 'a' and funkcja() # zwraca ostatnia prawde
print "a or funkcja() = ", 'a' or funkcja() # zwraca pierwsza prawde
print "---------------------------------------------------------------------"
# AND OR
print "0 and a or b =", 0 and 'a' or 'b' # zwroci b
print "Wyjasnienie: 0 and a or b => 0 or b => b"

print "1 and a or b =", 1 and 'a' or 'b' # zwroci a
print "Wyjasnienie: 1 and a or b => a or b => a"
print "---------------------------------------------------------------------"