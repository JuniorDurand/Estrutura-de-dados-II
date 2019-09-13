#from SelectionSort import SelectionSort 
#from insertionSort import InsertionSort 
#from ShellSort import ShellSort 
from MergeSort import MergeSort 


if __name__ == "__main__":

	#sr = SelectionSort()
	#sr = InsertionSort()
	sr = MergeSort()
	


	arr = [12,98,63,54,65,85,32,26,51,15,27,1] 
	print(arr)
	n = len(arr)
	sr.sort(arr)
	print ("Sorted array is:") 
	print(arr)