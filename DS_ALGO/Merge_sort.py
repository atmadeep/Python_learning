def MergeSort(num_list,left,right):
    if right-left<=1:
        return num_list[left:right] #base case.
    if right-left > 1:
        mid=(left+right)/2
        sublist1=MergeSort(num_list=num_list,left=left,right=mid)
        sublist2=MergeSort(num_list=num_list,left=mid,right=right)
        return merge(sublist1,sublist2)

def merge(A, B):
    (C,m,n)=([], len(A), len(B))
    (i,j)=(0,0)
    while i+j < m+n:
        if i==m:
            C.append(B[j])
            j+=1
        elif j==n:
            C.append(A[i])
            i+=1
        elif A[i] <= B[j]:
            C.append(A[i])
            i+=1
        elif A[i] >= B[j]:
            C.append(B[j])
            j+=1
    return (C)

a=[1,2,1,5,3,6,6,2,5,8,3,9,3]
print(a)
print(MergeSort(a,0,len(a)))