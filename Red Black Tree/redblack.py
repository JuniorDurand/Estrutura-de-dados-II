class Node(object):

	def __init__(self, data):
		self.data = data
		self.dad = None
		self.left = None
		self.right = None
		self.color = "red" #red or black


	def getColordad(self):
		if not self.dad is None:
			return self.dad.color
		else:
			return "black"

	def getDad(self):
		return self.dad





class RedBlack(object):

	def __init__(self, funCMP=None, funCMPKey = None):
		self.root = None

		if funCMP is None:
			self.cmp = self.defautCMP
		else:
			self.cmp = funCMP

		if funCMPKey is None:
			self.cmpKey = self.defautCMP
		else:
			self.cmpKey = funCMPKey

	def defautCMP(self, a, b):
		if (a > b):
			return -1
		elif(a < b):
			return 1
		else:
			return 0

	def getColor(self, Node):
		if not Node is None:
			return Node.color
		else:
			return "black"

	def __insert(self, data, Node):
		if not Node is None:

			stat = self.cmp(Node.data, data)


			if stat < 0:
				NewNode, Node.left = self.__insert(data, Node.left)
				Node.left.dad = Node
			else:
				NewNode, Node.right = self.__insert(data, Node.right)
				Node.right.dad = Node

			return NewNode, Node


		else:
			NewNode = Node(data)
			return NewNode, NewNode

	def __tio(self, Node):
		if Node.dad.dad.left == Node.dad:
			return Node.dad.dad.right
		else:
			return Node.dad.dad.left




	def __rb_insert_fixup(self, Node):
		
		#case 1
		if Node.dad is None:
			Node.color = "black"

		#caso 2
		elif Node.dad.color == "black":
			return

		#caso 3
		elif self.__tio(Node) != None and self.__tio(Node).color == "red":
			tio = self.__tio(Node)
			Node.dad.color = "black"
			tio.color = "black"
			avo = Node.dad.dad
			__rb_insert_fixup(avo)

		#caso 4 e 5
		else:
			tio = self.__tio(Node)
			avo = Node.dad.dad

			#caso 4
			if Node == Node.dad.right and Node.dad == avo.left:
				#rot esquerda Node.dad
				#Node = Node.left

			#caso 4
			elif  Node == Node.dad.left and Node.dad == avo.right:
				#rot direita Node.dad
				#Node = Node.right

			else:



		while Node.dad.color == "red":
			if Node.getDad() == Node.getDad().getDad().left:
				NodeAux = Node.getDad().getDad().right
				if self.getColor(NodeAux) == "red":
					Node.getDad().color = "black"
					if not NodeAux is None:
						NodeAux.color = "black"
					Node = 
			




	def insert(self, data):
		NewNode, self.root = self.__insert(data, self.root)




		

		