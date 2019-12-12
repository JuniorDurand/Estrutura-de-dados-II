class Vertex(object):
	def __init__(self, num):
		self.num = num
		self.listAdj = []
		self.listWeight = []
		self.pi = None
		self.alfa = None
		self.dist = None
		self.cor = "branco"


	def resetVertex(self):
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


	def containsEDGE(self, edge):
		if edge in self.listAdj:
			return True
		else:
			return False


	def getEDGEs(self):
		EDGEs = []
		for x in self.listAdj:
			EDGEs.append(x)

		return EDGEs

	def updateEDGE(self, edge, weight=1):
		index = self.listAdj.index(edge)
		if not index is None:
			self.listWeight[index] = weight
	

	def order(self, vertex):
		return vertex.num


	def ordenedVertex(self):
		self.listAdj.sort(key = self.order, reverse=True)


	def __str__(self):
		self.ordenedVertex()
		string = ""
		string += "%d :\n" % (self.num)
		for x in range(len(self.listAdj)):
			string += "\t %d, %.5f\n" % (self.listAdj[x].num, self.listWeight[x]) 
		return string


	def __repr__(self):
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


	def resetGraph(self):
		for x in self.vertex:
			x.resetVertex()


	def addEDGE(self, u, v, weight = None):
		if not self.containsEDGE(u, v):
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
		else:
			self.updateEDGE(u, v, weight)

	
	def removeEDGE(self, u, v):
		if self.oriented == "not_oriented":
			self.vertex[u].removeEDGE(self.vertex[v])
			self.vertex[v].removeEDGE(self.vertex[u])
		else:
			self.vertex[u].removeEDGE(self.vertex[v])


	def updateEDGE(self, u, v, weight = 1):
		if self.containsEDGE(u,v):
			if self.oriented == "not_oriented":
				self.vertex[u].updateEDGE(self.vertex[v], weight)
				self.vertex[v].updateEDGE(self.vertex[u], weight)
			else:
				self.vertex[u].updateEDGE(self.vertex[v], weight)



	
	def containsEDGE(self, u, v):
		return True if self.vertex[u].containsEDGE(self.vertex[v]) == True else False


	def __len__(self):
		return self.size


	def __str__(self):
		string = "[\n"
		for row in self.vertex:
			string += row.__str__()

		string += "]"
		return string


	def BFS(self, u = None):
		self.resetGraph()
		if u is None:
			u = self.vertex[0]
		else:
			u = self.vertex[u]

		queue = []
		#dist, Vertex.
		queue.append([0,u])
		while len(queue) > 0:
			#print(queue)
			count, u = queue.pop()
			EDGEs = u.getEDGEs()
			for EDGE in EDGEs:
				if EDGE.cor == "branco":
					queue.append([count+1,EDGE])
					EDGE.cor = "cinza"
					EDGE.dist = count+1
					EDGE.pi = u
			u.cor = "preto"

		queue = []
		#dist, Vertex
		queue.append([0,u])
		while len(queue) > 0:
			print(queue)
			count, u = queue.pop()
			EDGEs = u.getEDGEs()
			for EDGE in EDGEs:
				if EDGE.cor == "branco":
					queue.append([count+1,EDGE])
					EDGE.cor == "cinza"
					EDGE.pi = u
				u.cor = "preto"


