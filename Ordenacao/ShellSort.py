class ShellSort(object):

	def sort( self, start, col, end):
		h = 1
		while h < end - start:
			h = (3*h)+1

		while h > 0:
			h = (h-1)//3

			for i in range(h, end - start):
				temp = col[i]
				j=i

				while col[j-h] > temp:
					col[j] = col[j-h]
					j = j - h
					if (j < h):
						break

				col[j] = temp

		return col

