import collections
from collections import namedtuple

# point = namedtuple("point", "x y z h")
# point = namedtuple("point", ["x", "y", "z"])
point = namedtuple("point", {"x":0, "y":0, "z":0})


newP = point(3, 4, 5)
print(newP.x, newP.y, newP.z)
print(newP[0])
print(newP._asdict())
print(newP._fields)
print(newP._replace(y=6))
print(newP)

p2 = point._make(["a", "b", "c"])
print(p2)