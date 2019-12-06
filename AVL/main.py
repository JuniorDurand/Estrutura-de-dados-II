from avl import AvlTree

def printAvr(data):
	print(data)

av = AvlTree()
av.insert(2)
av.insert(10)
av.insert(2058)
av.insert(14)
av.insert(8206)

av.insert(8199)
print("=======")
av.visitSimet(printAvr)
print("=======")
av.visitPre(printAvr)


