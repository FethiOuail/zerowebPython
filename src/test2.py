# --------------------------
# ----  String Method  ----
# ---------------------------
from zeroweb.src.test1 import myString

name = "Anwar Kamel I am Developer"

len_name = len(name)

print('name length = ', len_name)
print(len(name))

print('-------------------------------')

names = name.split()
print(names)
# ---------------------------------
print('-------------------------------')
# strip() , rstrip(), lstrip()
myString = """      This is just test """
myTest = "###### This is test ###"
print(myString.strip())
print(myString.lstrip())
print(myString.rstrip())

print('----------------')
print(myTest.strip("#"))

# title
print('-------------- Title and  --------------')
myTitle = "i love 2d graphic and 2g technology and python"

print(myTitle.title())
print(myTitle.capitalize())
print('---------------------------')
print(myTitle)
myTitle = myTitle.title()
print(myTitle)

# ---------
print('----------------------')
a, b, c = "1", "11", "121"
print(a)
print(b)
print(c)

print(a.zfill(3))
print(b.zfill(3))
print(c.zfill(3))

n = "anwar"
print(n.upper())
print(n.lower())
print(name.find('Kamel'))

