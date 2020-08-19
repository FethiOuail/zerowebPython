
a = "Anwar Kamel I am Developer"
b =  "Anwar-Kamel-I-am-Developer"

print(a.split())
print(a.rsplit())

print(b.split('-',3))
print(b.rsplit('-',2))

print('---------- Center -------------')
# center()
c = "anwar"
print(c.center(9,"-"))
# count()
d = "I love Python and PHP , PHP is the Best, PHP "
print(d.count("o"))
print(d.count("PHP"))
print(d.count("PHP", 20))
print(d.count("PHP",0 , 25))

print('------ swapcase --------')
# swapcase()
e = "I LOve Python"
print(e.swapcase())

# satrtWith

print(e.startswith('I'))
print(e.startswith('P', 7,15))
print(e.endswith('n'))















