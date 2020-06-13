lst = [34, 33, 23]
lst += ["LOL"]

lst.pop()
lst.append(["34", "33"])
lst.extend(["34", "33"])
item = 33
print(item)
lst.remove(item)

x = lst
lst = "big fan"
# lst.pop() # error
y = x
y.append(4)
print(x[5]) # print 4
print(lst.pop()) # print 4
print(lst.pop()) # print 33
