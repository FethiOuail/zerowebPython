
# index(subString, start, End) and find(substring, start , end)

a = "I love Python"
b = """ My name
    is anwar
    kamel
    "ouail"""

print(a.index('P',5,10))
print(a.find('P'))
print(a.find("z"))


print(b.splitlines())

c = "Hi\tanwar\thow are you"
print(c)
print(c.expandtabs(10))
print(c.expandtabs(5))

print('----------------- replace() ------------------')
# replace(Old value, new , count)
d = "Hello how are you Anwar, Anwar are love me"
print(d)
print(d.replace('Anwar', 'Fethi', 1))

print('----------------- join() ------------------')
# join

mList = ['Anwar', 'kamel', 'Ouail']

print(mList)
s = " ".join(mList)
print(s)

mList2 = ['انور', 'كمال', 'وعيل']
print(mList2)
s2 = " ".join(mList2)
print(s2)



