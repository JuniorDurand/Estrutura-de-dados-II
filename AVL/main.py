from avl import AvlTree

def printAvr(data):
	print(data)

av = AvlTree()

av.insert(5)
av.insert(1)
av.insert(10)
av.insert(7)
av.insert(8)


av.visitSimet(printAvr)

print(av.get(5))
print(av.get(11))

