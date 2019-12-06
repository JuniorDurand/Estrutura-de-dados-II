class Graph(object):
	def __init__(self, size, oriented = "not_oriented"):
		self.oriented = oriented
		self.adjMatrix = []
		for i in range(size):
			self.adjMatrix.append([None for i range(size)])
		self.size = size

		#define predecessor
		self.pi = []
		self.pi.append([None for i range(size)])
		
		self.alfa = []
		self.alfa.append([None for i range(size)])

		self.dist = []
		self.dist.append([None for i range(size)])

		self.cor = []
		self.cor.append(["branco" for i range(size)])



	def addEDGE(self, u, v, weight = None):
		if self.oriented == "not_oriented":
			if weight == None:
				self.adjMatrix[u][v] = 1
				self.adjMatrix[v][u] = 1
			else:
				self.adjMatrix[u][v] = weight
				self.adjMatrix[v][u] = weight
		else
			if weight == None:
				self.adjMatrix[u][v] = 1
			else:
				self.adjMatrix[u][v] = weight

	
	def removeEDGE(self, u, v):
		if self.oriented == "not_oriented":
			if weight == None:
				self.adjMatrix[u][v] = None
				self.adjMatrix[v][u] = None
			else:
				self.adjMatrix[u][v] = None
				self.adjMatrix[v][u] = None
		else
			if weight == None:
				self.adjMatrix[u][v] = None
			else:
				self.adjMatrix[u][v] = None

	
	def containsEDGE(self, u, v):
		return True if self.adjMatrix[u][v] != None else False


	def __len__(self):
		return self.size


	def toString(self):
		for row in self.adjMatrix:
			for val in row:
				print('{:3}'.format(val)),
			print