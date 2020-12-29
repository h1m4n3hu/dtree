arr=[3,3,1,3,4,5,4]

def selsort():
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)

def recur_selsort(i):
    if i+1>len(arr):return
    temp = i
    for j in range(i,len(arr)):
        if arr[temp] > arr[j]:
            temp = j
    arr[temp], arr[i] = arr[i], arr[temp]
    print(arr)
    recur_selsort(i+1)

def bubsort():
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            print(arr)
        print("!!")

def recur_bubsort(n):
    if n==0:
        return
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
        print(arr)
    recur_bubsort(n-1)

def inssort():
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        print(arr)

def mrgsort(arr):
    if len(arr)<=1 and arr is not None:
        return arr
    left=arr[:len(arr)//2]
    right=arr[len(arr)//2:]
    print(left,right,"ijuhgf")
    left=mrgsort(left)
    right=mrgsort(right)

    i=j=0
    sorted=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            sorted.append(left[i])
            i+=1
        else:
            sorted.append(right[j])
            j+=1
    while i<len(left):
        sorted.append(left[i])
        i+=1
    while j<len(right):
        sorted.append(right[j])
        j+=1
    return sorted

def part(arr,low,high):
    i=low-1
    pivot=high
    for j in range(low,high):
        if arr[j]<arr[pivot]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        #print(arr)
    arr[i+1],arr[pivot]=arr[pivot],arr[i+1]
    return i+1

def qksort(arr,low,high):
    if low<high:
        pp=part(arr,low,high)
        qksort(arr,low,pp)
        qksort(arr,pp+2,high)

def countsort():
    op=[0]*len(arr)
    zer=[0]*len(arr)
    for i in arr:
        zer[i]+=1

    for i in range(1,len(zer)):
        zer[i]+=zer[i-1]

    

    i=len(arr)-1
    while i>=0:
        op[zer[arr[i]]-1]=arr[i]
        zer[arr[i]]-=1
        i-=1
    print(op)

countsort()