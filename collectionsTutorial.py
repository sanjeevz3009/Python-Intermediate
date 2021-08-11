import collections
from collections import Counter

# c = Counter("gallad")
# print(c)
# c = Counter(["a", "a", "b", "c", "c"])
# print(c)
# c = Counter({"a": 1, "b": 2})
# print(c)
# c = Counter(cats=4, dogs=7)
# Doesn't throw an error when a key doesn't exist
# print(c['meow'])
# print(list(c.elements()))
# print(c.most_common())

# c = Counter(a=4, b=2, c=0, d=-2)
# d = ["a", "b", "b", "c"]
# c.subtract(d)
# c.update()
# print(c)
# c.clear()
# print(c)

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(["a", "b", "b", "c"])

print(c+d)
print(c-d)
print(c & d)
print(c | d)