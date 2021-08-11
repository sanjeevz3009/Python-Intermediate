l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x):
	return x**x

# newList = []
# for x in l:
# 	newList.append(func(x))

# print(newList)

# Does the same thing above in one line
#print(list(map(func, l)))

# Or you can do a list comprehension
print([func(x) for x in l if x%2==0])