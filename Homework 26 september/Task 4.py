A = list(map(int, input()))
i=0
while i < len(A):
    A.insert(i+2, A[i])
    A.pop(i)
    i = i+2
print(A)