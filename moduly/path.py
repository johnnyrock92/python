import sys

print sys.path
print len(sys.path)
sys.path.append('C:\modules')

print "----------------------------------------------------------------------------------"
print sys.path
print len(sys.path)