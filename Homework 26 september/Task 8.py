n = int(input())
A = list(map(int, input().split()))
b = 0
m = 0
med = 0
for i in range(n):
    for j in range(n):
        if A[i]<A[j]:
            m+=1
        elif A[i]>A[j]:
            b+=1
        if (b==((n-1)/2)) and (m==((n-1)/2)):
            med = A[i]
    m = 0
    b = 0
print(med)
