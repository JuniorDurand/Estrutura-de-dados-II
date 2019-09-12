#from SelectionSort import SelectionSort 
#from insertionSort import InsertionSort 
from shellSort import ShellSort 


if __name__ == "__main__":

	#sr = SelectionSort()
	#sr = InsertionSort()
	sr = ShellSort()
	


	arr = [12,98,63,54,65,85,32,26,51,15,27] 
	print(arr)
	n = len(arr)
	sr.sort(0,arr,n)
	print ("Sorted array is:") 
	print(arr)