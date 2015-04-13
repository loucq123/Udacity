# The reason why to use generator expression
#
# 1. We can use less indentation
# 2. Stop early
# 3. It is easier to edit

def sq(x):
	print ("sq called", x)
	return x * x

g = (sq(x) for x in range(10) if x%2 == 0)
print (g)

next(g)
next(g)
next(g)
next(g)
next(g)
next(g)  # Raise a StopIterations for g is at the end.

# Using a for loop so that we never have to deal explicitly with those StopIterations.
for x2 in (sq(x) for x in range(10) if x%2 == 0):
	pass
	''' output is:
		sq called 0
		sq called 2
		sq called 4
		sq called 6
		sq called 8'''

print (list((sq(x) for x in range(10) if x%2 == 0)))
# output is [0, 2, 4, 6, 8]