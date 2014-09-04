def main ():
    inp = input('--> ')
    A = inp.split()
    A = list(map(int,A))
    QuickSort(A,0,len(A)-1)
    print(A)

def QuickSort(A,p,r):
    if p < r:
        q = Partition(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)

def Partition(A,p,r):
    i = p-1
    for j in range(p,r,1):
        if A[j] <= A[r]:
            i+=1
            A[i],A[j] = A[j], A[i]
    A[r],A[i+1] = A[i+1],A[r]
    return i+1
