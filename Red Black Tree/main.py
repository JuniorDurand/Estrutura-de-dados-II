from redblack import RedBlack

def printAvr(data):
	print(data)

av = RedBlack()


def defautCMP( a, b):
	if (a > b):
		return -1
	elif(a < b):
		return 1
	else:
		return 0



av.insert(12)
av.insert(8)
av.insert(18)
av.insert(5)
av.insert(11)
av.insert(17)
av.insert(4)
av.insert(7)


print("Simetrica")
av.simmetric()


av.insert(2)

print("-----------")

print("Simetrica")
av.simmetric()



"""

from redblack import RedBlack

def printAvr(data):
	print(data)

av = RedBlack()


def defautCMP( a, b):
	if (a > b):
		return -1
	elif(a < b):
		return 1
	else:
		return 0



av.insert(12, defautCMP)
av.insert(8, defautCMP)
av.insert(18, defautCMP)
av.insert(5, defautCMP)
av.insert(11, defautCMP)
av.insert(17, defautCMP)
av.insert(4, defautCMP)
av.insert(7, defautCMP)


print("Simetrica")
av.simmetric()


av.insert(2, defautCMP)

print("-----------")

print("Simetrica")
av.simmetric()
"""