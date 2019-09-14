from insertionSort import InsertionSort

class MergeSortFinalInsert(object):

	def __init__(self, L):
		self.insert = InsertionSort()
		self.L = L

	
	def setL(self, L):
		self.L = L

	
	def sort(self,  col, start = 0, end = None): 
		if len(col) >1:
			mid = len(col)//2 
			colL = col[:mid]
			colR = col[mid:]

			if len(colL) < self.L and len(colR) < self.L:
				self.insert.sort(colL)
				self.insert.sort(colR)
			else:
				self.sort(colL)
				self.sort(colR) 


			i = 0
			j = 0
			k = 0

			while i < len(colL) and j < len(colR): 
				if colL[i] < colR[j]: 
					col[k] = colL[i] 
					i+=1
				else: 
					col[k] = colR[j] 
					j+=1
				k+=1

			# Checking if any element was left 
			while i < len(colL): 
				col[k] = colL[i] 
				i+=1
				k+=1

			while j < len(colR): 
				col[k] = colR[j] 
				j+=1
				k+=1

