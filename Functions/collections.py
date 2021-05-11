from collections import Counter

c = Counter("Hallo")
print(c)
print(list(c.elements()))
c = Counter(["Peter", "Max", "Schmitz","Peter"])
print(list(c.most_common()))
print(c)
c = Counter({"name": "Max", "age": 12, "age": 24})
print(c)
c = Counter(cats=4, dogs=5)

print(list(c.most_common(1)))

Counter.__dict__