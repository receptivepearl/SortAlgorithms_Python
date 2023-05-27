# main.py
lenList = 10000
timesSort = 20
import random
import time
# Selection sort
def selectionSort(lst):
  for i in range(len(lst)):
    maxItem = lst[i]
    maxItemI = i
    for j in range(i, len(lst)):
      if lst[maxItemI]<lst[j]:
        maxItem=lst[j]
        maxItemI=j
    old=lst[i] 
    lst[i]=lst[maxItemI]
    lst[maxItemI]=old
  return lst
# Insertion sort
def insertionSort(lst):
  for i in range(len(lst)):
    key=lst[i]
    j = i-1
    while j > -1 and key < lst[j]:
      lst[j+1]=lst[j]
      j-=1
    lst[j+1]=key
  return lst
# Bubble sort
def bubbleSort(unsorted):
  for j in range(1,len(unsorted)):
    for i in range(0,len(unsorted)-j):
      if unsorted[i] > unsorted[i+1]:
        unsorted[i], unsorted[i+1] = unsorted[i+1], unsorted[i]
  return unsorted
# Merge sort - divide and conquer
def merge(list1,list2):
  sortedList=[]
  while len(list1) != 0 and len(list2)!=0:
    if list1[0]<list2[0]:
      sortedList.append(list1.pop(0))
    else:
      sortedList.append(list2.pop(0))
  return sortedList+list2+list1
def mergeSort(unsortedList):
  if len(unsortedList)<=1:
    return unsortedList
  else:
    midPoint=len(unsortedList)//2
    leftHalf=mergeSort(unsortedList[0:midPoint])
    rightHalf=mergeSort(unsortedList[midPoint:])
    return merge(leftHalf,rightHalf)
# Quick sort (pivot being first element) - partition
def partition(lst, pivot):
  less, eq, great = [[] for i in range(3)]
  for i in range(len(lst)):
    if lst[i]<pivot:
      less.append(lst[i])
    if lst[i]==pivot:
      eq.append(lst[i])
    if lst[i]>pivot:
      great.append(lst[i])
  return less, eq, great
  
def quickSort(unsorted):
  if len(unsorted)<=1:
    return unsorted
  pivot=unsorted[0]
  first=unsorted[0]   
  middle=unsorted[len(unsorted)//2]
  last=unsorted[-1]
  if first>middle:
    if first<last:
      pivot=first
    elif middle>last:
      pivot=middle
    else:
      pivot=last
  else:
    if first>last:
      pivot=first
    elif middle<last:
      pivot=middle
    else:
      pivot=last
  less,eq,great=partition(unsorted,pivot)
  return quickSort(less)+eq+quickSort(great)
# Quick sort (pivot being optimized)

# random list
testList=[random.randint(1,100) for i in range(lenList)]
testList1=testList.copy()

print("Random List")

start=time.time()
selectionSort(testList1)
print("Selection:  "+str(time.time()-start))
testList1=testList.copy()
start=time.time()
insertionSort(testList1)
print("Insertion:  "+str(time.time()-start))
testList1=testList.copy()
start=time.time()
bubbleSort(testList1)
print("Bubble:  "+str(time.time()-start))
testList1=testList.copy()
start=time.time()
mergeSort(testList1)
print("Merge:  "+str(time.time()-start))
testList1=testList.copy()
start=time.time()
quickSort(testList1)
print("Quick:  "+str(time.time()-start))
# random,sorted,reverse sorted
# sorted
testList=[random.randint(1,100) for i in range(lenList)]
testList.sort()

print("Sorted List")
testList1=testList.copy()
start=time.time()
selectionSort(testList1)
print("Selection:  "+str(time.time()-start))
testList1=testList.copy()
start=time.time()
insertionSort(testList1)
print("Insertion:  "+str(time.time()-start))
testList1=testList.copy()
start=time.time()
bubbleSort(testList1)
print("Bubble:  "+str(time.time()-start))
testList1=testList.copy()
start=time.time()
mergeSort(testList1)
print("Merge:  "+str(time.time()-start))
testList1=testList.copy()
start=time.time()
quickSort(testList1)
print("Quick:  "+str(time.time()-start))
# reverse
testList=[random.randint(1,100) for i in range(lenList)]
testList.sort()
testList.reverse()

print("Reverse List")
testList1=testList.copy()
start=time.time()
selectionSort(testList1)
print("Selection:  "+str(time.time()-start))
testList1=testList.copy()
start=time.time()
insertionSort(testList1)
print("Insertion:  "+str(time.time()-start))
testList1=testList.copy()
start=time.time()
bubbleSort(testList1)
print("Bubble:  "+str(time.time()-start))
testList1=testList.copy()
start=time.time()
mergeSort(testList1)
print("Merge:  "+str(time.time()-start))
testList1=testList.copy()
start=time.time()
quickSort(testList1)
print("Quick:  "+str(time.time()-start))
