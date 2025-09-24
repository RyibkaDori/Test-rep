A = list(map(int, input()))
A.insert(0, A[len(A) - 1])
A.pop()
print(A)