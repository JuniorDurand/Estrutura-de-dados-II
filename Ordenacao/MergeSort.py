class MergeSort(object):



	def sort(self,  col, start = 0, end = None): 
		if len(col) >1:
			mid = len(col)//2 
			colL = col[:mid]  
			colR = col[mid:]

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

			while i < len(colL): 
				col[k] = colL[i] 
				i+=1
				k+=1

			while j < len(colR): 
				col[k] = colR[j] 
				j+=1
				k+=1

		return col

