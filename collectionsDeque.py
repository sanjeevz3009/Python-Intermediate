import collections
from collections import deque

# d = deque("hello")
# d.append("4")
# d.appendleft(5)
# print(d)

# d.pop()
# d.popleft()

# d.clear()
# print(d)

# d.extend('456')
# d.extend("hello")
# d.extend([1, 2, 3])
# d.extendleft("hey")
# print(d)

# d.rotate(2)
# # d.reverse()
# print(d)

d = deque("hello", maxlen=5)
print(d)
# d.append(1)
d.extend([1, 2, 3])
print(d)