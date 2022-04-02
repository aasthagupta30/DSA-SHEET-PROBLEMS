def findSimilarity(A, B, n, m):
    count=0
    count1=0
    list1=[]
    for i in range(n):
        for j in range(m):
            if (A[i] == B[j]):
                count=count+1
    list1.append(count)
    list1.append(n+m-count)
    return list1
    
    pass
