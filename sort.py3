import random
def quicksort(array,start,stop):
	if start<stop:
		pivotindex=pivotindexs(array,start,stop)
		quicksort(array,start,pivotindex-1)
		quicksort(array,pivotindex+1,stop)
def pivotindexs(array,start,stop):
	pivot=random.randint(start,stop)
	array[start],array[pivot]=array[pivot],array[start]
	return partition(array,start,stop)
def partition(array,start,stop):
	i=start+1
	pivot=array[start]
	for j in range(start+1,stop-1):
		if array[j]<=pivot:
			array[j],array[i]=array[i],array[j]
			i=i+1
	array[i-1],pivot=pivot,array[i-1]
	pivot=i-1
	return pivot
if __name__ == '__main__':
	n=int(input())
	arr = list(map(int,input(" ").strip().split()))[:n]
	quicksort(arr,0,n-1)
	for i in range(0,n):
		print(arr[i],end=" ")
