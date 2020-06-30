""" Nonlocal and Global (no it's not geography, there's also Mutability)"""

"""
In a frame that isn't the global frame, using the code
global x
allows you to modify the global variable x

In the same way, using
local x
allows you to modify the parent frame's local variables
"""
x = 42
def harhar():
	fib = 0
	the = "Yeeted"

	def new_thing():
		# nonlocal the
		fib = 1
		# the = "Yote"
		# x = the + " Yee"
		def f():
			nonlocal the
			the = "yeet"
			return the
		return f()

	print(new_thing())
	# x = the + " outta here"
	return the, fib

print(harhar())

y = 1
def setup():
	global a, y
	a = [3, 4, 5]
	y = a
	print(y)

setup()
a = a + [2]
print(a)
print(y)

setup()
a += [6]
print(a)
print(y)

setup()
a.append([5, 6])
print(a)
print(y)

setup()
a.extend([5, 6])
print(a)
print(y)

setup()
x = a.copy()
# a.remove(23)
a.remove(3)
print(a)
print(y)
print(x)

setup()
a.insert(1, 1)
print(a)
print(y)

setup()
a.pop(2)
print(a)
print(y)

"""
Nonmutating:
		lst.copy() # Return a copy of lst
		[] + [] # concatenates the two lists (does not modify old lists, instead returns new combined list)


Mutating:


	The following all return None:
		lst.append(x) # Adds x to the end of lst
		lst.extend(x) # Concatenates x (x must be a list) to lst (flattens x)
		lst.remove(x) # Removes the first occurrence of x in lst, otherwise errors
		lst.insert(x, i) # Insert x at index i (does not replace element, adds new one)

		lst += lst2 # the equivalent of calling extend(lst2) on lst

	This returns the element it pops:
		lst.pop(i) # Removes and returns the element at index i
"""
