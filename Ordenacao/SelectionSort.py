class SelectionSort(object):

	def sort( self, col, start=0,  end=None):
		if end == None:
			end = len(col)
			
		for i in range(start,end):
			min = i
			for j in range(i+1, end):
				if col[j] < col[min] :
					min = j

			temp = col[min]
			col[min] = col[i]
			col[i] = temp

		return col

"""
	def sort( self,  col):
		start = 0
		end = len(col)
		for i in range(start,end):
			min = i
			for j in range(i+1, end):
				if col[j] < col[min] :
					min = j

			temp = col[min]
			col[min] = col[i]
			col[i] = temp

		return col
"""