class MergeSort(object):


	def sort(self, col): 
		if len(col) >1:
			mid = len(col)//2 #Finding the mid of the colay 
			colL = col[:mid] # Dividing the colay elements  
			colR = col[mid:] # into 2 halves 

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

	def sort(self,  col, start = 0, end = None): 
		if len(col) >1:
			mid = len(col)//2 #Finding the mid of the colay 
			colL = col[:mid] # Dividing the colay elements  
			colR = col[mid:] # into 2 halves 

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

