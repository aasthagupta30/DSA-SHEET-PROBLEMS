def kthSmallLarge(arr, n, k):
    arr.sort()
    new=[]
    new.append(arr[k-1])
    new.append(arr[n-k])
    return new
