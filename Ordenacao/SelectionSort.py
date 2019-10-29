class SelectionSort(object):


	def sort(self, vet):
		for i in range(len(vet)-1):
			print(vet)
			menor = i
			temp = vet[menor]
			for j in range(i+1,len(vet)):
				if vet[menor]>vet[j]:
					menor = j

			temp = vet[menor]
			j = menor
			while j>0 and j>i:
				vet[j] = vet[j-1]
				j-=1
			vet[j] = temp

		return vet

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

"""
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