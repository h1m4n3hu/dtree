arr=[5,4,1,3,7,10,2]

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


def mergeSort(a):
    current_size = 1

    while current_size < len(a) - 1:

        left = 0
        while left < len(a) - 1:
            mid = min((left + current_size - 1), (len(a) - 1))
            print(mid,"mid")

            right = ((2 * current_size + left - 1, len(a) - 1)[2 * current_size + left - 1 > len(a) - 1])
            print(right,"right")

            print(left,"left")

            merge(a, left, mid, right)
            left = left + current_size * 2
            print(left,"left")
            print("=== === ===")

        current_size = 2 * current_size


def merge(a, left, mid, right):
    n1 = mid - left + 1
    print(n1,end="_  ")
    n2 = right - mid
    print(n2,end="_  ")
    L = [0] * n1
    print(L,end="  ")
    R = [0] * n2
    print(R,end="  ")
    for i in range(0, n1):
        L[i] = a[left + i]
    print(L,end="  ")
    for i in range(0, n2):
        R[i] = a[mid + i + 1]
    print(R)

    i, j, k = 0, 0, left
    while i < n1 and j < n2:
        if L[i] > R[j]:
            a[k] = R[j]
            j += 1
        else:
            a[k] = L[i]
            i += 1
        k += 1

    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1
    print(a)


