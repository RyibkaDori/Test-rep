A = list(map(int, input()))
max=A[1]
for i in range(len(A)):
    if A.count(A[i])>A.count(max):
        max = A[i]
print(max)
