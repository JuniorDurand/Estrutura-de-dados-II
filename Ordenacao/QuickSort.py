class Quicksort(object):

	def sort( self, col, start=0,  end=None):
		if end == None:
			end = len(col) -1
		
		if start < end:
			part = self.partition(col, start, end)
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






"""
algorithm quicksort(A, lo, hi) is
    if lo < hi then
        p := particiona(A, lo, hi)
        quicksort(A, lo, p – 1)
        quicksort(A, p + 1, hi)

algorithm particiona(A, lo, hi) is
    pivot := A[hi]
    i := lo - 1    
    for j := lo to hi - 1 do
        if A[j] < pivot then
            i := i + 1
            swap A[i] with A[j]
    if pivot < A[i + 1] then
        swap A[i + 1] with A[hi]
    return i + 1
"""
