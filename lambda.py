# def func(x):
# 	return x+5

# func2 = lambda x: x+5
# print(func2(9))
# print(func(2))

# def func(x):
# 	func2 = lambda x: x+5
# 	return func2(x) + 85

# Optional parameters are possible
# func3 = lambda x, y=4: x+y
# print(func3(5, 5))

# print(func(2))

# Saves a lot of lines of code, more efficient
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

newList = list(map(lambda x: x+5, a))
print(newList)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# newList = list(filter(lambda x: x%2==0, a))
# print(newList)