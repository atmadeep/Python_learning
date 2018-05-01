def QuickSort(A,l,r):
    if r-l <=1:
        return ()
    yellow = l+1

    for green in range(l+1,r):
        if A[green] <= A[l]:
            (A[yellow],A[green]) = (A[green],A[yellow]) #swapping.
            yellow+=1

    (A[l],A[yellow-1])=(A[yellow-1],A[l])  #move the pivot in place.
    QuickSort(A,l,yellow-1)
    QuickSort(A,yellow,r)

a = [1,7,5,3,8,2,7,8,9,3,6]
QuickSort(a,0,len(a))
print(a)