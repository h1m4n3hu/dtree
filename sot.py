arr=[10,2,12,4,21,3,5,6,9]

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

def inssort(arr):
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


def countsort2(arr,pv):
    op=[0]*len(arr)
    zer=[0]*10

    for i in range(0,len(arr)):
        zer[(arr[i]//pv)%10]+=1

    for i in range(1,len(arr)):
        zer[i]+=zer[i-1]

    i=len(arr)-1
    while i>=0:
        print(zer[(arr[i]//pv)%10]-1,end=" ")
        print(arr[i])
        op[zer[(arr[i]//pv)%10]-1]=arr[i]
        zer[(arr[i]//pv)%10] -=1
        i-=1
    print(op)

    i = 0
    for i in range(0, len(arr)):
        arr[i] = op[i]
    print(op)

def radixort(arr):
    max1 = max(arr)

    exp = 1
    while max1 / exp > 0:
        countsort2(arr, exp)
        exp *= 10

def insersort(arr):
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while j>=0 and temp<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp

lst=[]
def bucksort():
    for i in range(0,10):
        lst.append([])

    for i in arr:
        lst[int(i*10)].append(i)

    k=[]
    for i in lst:
        insersort(i)
        if i is not None:
            k.extend(i)
    print(k)


def shellSort(arr):
    gap=3
    while gap>0:
        for i in range(gap,len(arr)):
            temp=arr[i]
            j=i
            while temp<arr[j-gap] and j>=gap:
                arr[j]=arr[j-gap]
                j-=gap
            arr[j]=temp
        gap-=1



def calcMinRun(n):
    r = 0
    while n >= 32:
        r = r | n&1
        n = n>>1
    return n + r

def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1

def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)
    # minRun2=calcMinRun(len(arr2))
    # print(minRun2)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)
    # for i in range(0,len(arr2),minRun2):
    #     try:
    #         print(arr2[i],"yyyy",end="  ")
    #     except:
    #         pass

    size = minRun
    print(size,n,"asdfasdfasdf")
    while size < n:

        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            merge(arr, left, mid, right)

        size = 2 * size



if __name__ == "__main__":
    arr = [-2, 7, 15, -14, 0, 15, 0, 7, -7, -4, -13, 5, 8, -14, 12]
    # arr2=[i for i in range(0,90)]
    print(arr)
    timSort(arr)
    print(arr)