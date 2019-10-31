from redblack import RedBlack

def printAvr(data):
	print(data)

av = RedBlack()

av.insert(12)
av.insert(8)
av.insert(18)
av.insert(5)
av.insert(11)
av.insert(17)
av.insert(4)
av.insert(7)


print("Simetrica")
av.visitSimet(printAvr)
print("Pre ordem")
av.visitPre(printAvr)

av.insert(2)

print("-----------")
print("Simetrica")
av.visitSimet(printAvr)
print("Pre ordem")
av.visitPre(printAvr)
