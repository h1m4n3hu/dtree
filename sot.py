arr=[3,8,1,9,4,5,7]
arr2=[3,8,1,9,4,5,7]

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

def part(arr,low):
    i=low-1
    pivot=len(arr)-1
    for j in range(low,len(arr)):
        if arr[j]<arr[pivot]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        print(arr)
    arr[i+1],arr[j]=arr[j],arr[i+1]
    print(arr)
part(arr2,0)

def qksort():
    pass
