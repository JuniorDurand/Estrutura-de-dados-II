class InsertionSort(object):

	def sort( self, start, col, end):
		for j in range(start,end):
			key = col[j]

			i = j -1
			while i >= 0 and col[i] > key:
				col[i+1] = col[i]
				i-=1

			col[i+1] = key
			
		return col

