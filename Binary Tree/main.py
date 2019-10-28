from tree import BTree
def visit(data):
	print(data)

tree = BTree()

tree.insert(2)
tree.visitSimet(visit)
print("----------")
tree.insert(1)
tree.visitSimet(visit)
print("----------")
tree.insert(3)
tree.visitSimet(visit)
print("----------")


def cmp(data1, data2):
	if data1 > data2:
		return -1
	elif data1 < data2:
		return 1
	else:
		return 0

tree.visitSimet(visit)
tree.remove(2, cmp)
tree.visitSimet(visit)