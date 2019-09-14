from insertionSort import InsertionSort 

class QuicksortFinalInsert(object):

	def __init__(self, L):
		self.insert = InsertionSort()
		self.L = L

	def setL(self, L):
		self.L = L

	def sort( self, col, start=0,  end=None):
		if end == None:
			end = len(col) -1
		
		if start < end:

			part = self.partition(col, start, end)
			if part - start < self.L and end - part < self.L:
				
				self.insert.sort(col, start, part)
				self.insert.sort(col, part +1, end)
			else:

				self.sort(col, start, part-1)
				self.sort(col, part+1, end)

		return col

	def partition(self, col, start, end):
		pivot = col[end]
		i = start-1

		for j in range(start, end):
			if col[j] < pivot:
				i+=1
				col[j], col[i] = col[i], col[j]

		if pivot < col[i+1]:
			col[i+1], col[end] = col[end], col[i+1]

		return i +1



