#from SelectionSort import SelectionSort 
#from insertionSort import InsertionSort 
#from ShellSort import ShellSort 
#from MergeSort import MergeSort 
#from QuickSort import Quicksort 
#from QuickSortFinalInsert import QuicksortFinalInsert 
#from QuickSortPartialInsert import QuickSortPartialInsert 
#from MergeSortPartialInsert import MergeSortPartialInsert 
from MergeSortFinalInsert import MergeSortFinalInsert 


if __name__ == "__main__":

	#sr = SelectionSort()
	#sr = InsertionSort()
	#sr = ShellSort()
	#sr = MergeSort()
	#sr = Quicksort()
	#sr = QuicksortFinalInsert(3)
	#sr = QuickSortPartialInsert(3)
	#sr = MergeSortPartialInsert(3)
	sr = MergeSortFinalInsert(3)
	


	arr = [12,98,63,54,65,85,32,26,51,15,27,1] 
	print(arr)
	n = len(arr)
	sr.sort(arr)
	print ("Sorted array is:") 
	print(arr)