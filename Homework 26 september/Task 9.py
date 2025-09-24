with open('input.txt', 'r') as infile1:
    L1 = infile1.read()
    A = L1.replace('!', '.')
    C = A.replace('?', '.')
    B = C.replace('...', '.')
    D = B.replace('..', '.')
    S = list(D.split('.'))
print(len(S)-1)

'''
sentences = 0
with open('input.txt', 'r') as infile1:
    L1 = infile1.read()
print(L1)
for s in L1:
    if s=='?':
        sentences += 1
    elif s=='!':
        sentences += 1
    elif s=='.':
        sentences += 1
    elif s=='...':
        sentences += 1
    elif s=='!?':
        sentences += 1
    elif s=='?!':
        sentences += 1
print(sentences)
'''