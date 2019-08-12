def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):#it is done as by every pass  the last element already gets sorted
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

def optimize_bubble(arr):#O(n*n) in general but stops if inner loop does not cause any change
    n=len(arr)    
    for i in range(n):
        swapped=False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]               
                swapped=True
        if swapped==False:
            break
def selection(arr):
    for i in range(len(arr)-1,0,-1):#output for n=5,[4,3,2,1,0] as last element already sorted at every pass
        max=0
        for j in range(1,i+1):
            if arr[j]>arr[max]:
                max=j
        arr[max],arr[i]=arr[i],arr[max]
def insertion(arr):
    for i in range(1,len(arr)):
        cval=arr[i] #extract from unsorted list
        pos=i
        while pos>0 and arr[pos-1]>cval:
            arr[pos]=arr[pos-1] #ifcurrent is greater than extracted then move element towads right
            pos=pos-1
        arr[pos]=cval #otherwise insert extracted element
###### SHELL SORT###########
#shell sort is the both combination of shell and insertion       
def shell(arr):
    sublistc=len(arr)//2
    while sublistc>0:
        for start in range (sublistc):
            gap_insertion(arr,start,sublistc)
        sublistc=sublistc//2
def gap_insertion(arr,start,gap):
    for i in range(start+gap,len(arr),gap):
        cval=arr[i]
        pos=i
        while pos>0 and arr[pos-gap]>cval:
            arr[pos]=arr[pos-gap]
            pos=pos-1
        arr[pos]=cval
#######**************#############*************##############################
def merge(arr):
    if len(arr)>1:
        
        mid=len(arr)//2
        leftarr=arr[:mid]#half the list
        rightarr=arr[mid:]
        merge(leftarr) #sorting and merging left part
        merge(rightarr) #sorting and merging right part
        i=0
        j=0
        k=0
        while i< len(leftarr) and j < len(rightarr): #comparing and merging adjacent
            if leftarr[i]<rightarr[j]:
                arr[k]=leftarr[i]
                i+=1
            else:
                arr[k]=rightarr[j]
                j+=1
            k+=1
            
        while i<len(leftarr):#merging sorted on left part
            arr[k]=leftarr[i]
            i+=1
            k+=1
        while j<len(rightarr): #merging sorted on right part
            arr[k]=rightarr[j]
            j+=1
            k+=1
def quick(arr):
    quick_help(arr,0,len(arr)-1)
def quick_help(arr,first,end):
    if first<end:
        splitpoint=partition(arr,first,end)
        quick_help(arr,first,splitpoint-1)
        quick_help(arr,splitpoint+1,end)
def partition(arr,first,end):
    pivot=arr[first]
    leftmark=first+1
    rightmark=end
    done=False
    while not done:
        while leftmark<=rightmark and arr[leftmark]<=pivot:
            leftmark+=1
        while rightmark>=leftmark and arr[rightmark]>=pivot:
            rightmark-=1
        if rightmark<leftmark:
            done=True
        else:
            arr[leftmark],arr[rightmark]=arr[rightmark],arr[leftmark]
    arr[first],arr[rightmark]=arr[rightmark],arr[first]
    return rightmark
arr=[1,5,8,7,6,3]
quick(arr)
print(arr)