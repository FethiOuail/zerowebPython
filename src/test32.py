# ------------------------
# -- Dictionary Methods --
# ------------------------

# setdefault()

user = {
  "name": "Osama"
}
print(user)
print(user.setdefault("age", 36))
print(user)

print("=" * 40)

# popitem()

member = {
  "name": "Osama",
  "skill": "PS4"
}

print("-" * 40)
print(member)
member.update({"age": 36})
print(member.popitem())
print("--" * 40)
print("=" * 40)

# items()

view = {
  "name": "Osama",
  "skill": "XBox"
}

allItems = view.items()
print(view)
view["age"] = 36

print(allItems)

print("=" * 40)

# fromkeys()

a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = "X"

c = ('name', 'email', 'password')
d = ['anwar', 'anwar@anwar', '12345678']

print(dict.fromkeys(a, b))

print(dict.fromkeys(c, d))
