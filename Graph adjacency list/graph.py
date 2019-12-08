class Vertex(object):
	def __init__(self, num = 0):
		self.num = num
		self.listAdj = []
		self.listWeight = []
		self.pi = None
		self.alfa = None
		self.dist = None
		self.cor = "branco"

	def addEDGE(self, edge, weight=1):
		self.listAdj.append(edge)
		self.listWeight.append(weight)

	def removeEDGE(self, edge):
		index = self.listAdj.index(edge)
		if not index is None:
			self.listAdj.pop(index)
			self.listWeight.pop(index)

	def __str__(self):
		string = ""
		string += "%d :\n" % (self.num)
		for x in range(len(self.listAdj)):
			string += "\t %d, %.5f\n" % (self.listAdj[x].num, self.listWeight[x]) 
		return string

		

class Graph(object):
	def __init__(self, size, oriented = "not_oriented"):
		self.oriented = oriented
		self.vertex = []
		for i in range(size):
			self.vertex.append(Vertex(num=i))
		self.size = size




	def addEDGE(self, u, v, weight = None):
		if self.oriented == "not_oriented":
			if weight == None:
				self.vertex[u].addEDGE(self.vertex[v])
				self.vertex[v].addEDGE(self.vertex[u])
			else:
				self.vertex[u].addEDGE(self.vertex[v], weight = weight)
				self.vertex[v].addEDGE(self.vertex[u], weight = weight)
		else:
			if weight == None:
				self.vertex[u].addEDGE(self.vertex[v])
			else:
				self.vertex[u].addEDGE(self.vertex[v], weight = weight)

	
	def removeEDGE(self, u, v):
		if self.oriented == "not_oriented":
			self.vertex[u].removeEDGE(self.vertex[v])
			self.vertex[v].removeEDGE(self.vertex[u])
		else:
			self.vertex[u].removeEDGE(self.vertex[v])
	
	def containsEDGE(self, u, v):
		return True if self.vertex[u].listAdj.index(self.vertex[v]) != None else False


	def __len__(self):
		return self.size


	def __str__(self):
		string = "[\n"
		for row in self.vertex:
			string += row.__str__()

		string += "]"
		return string