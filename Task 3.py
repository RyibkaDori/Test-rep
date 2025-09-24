C=[ 'A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']
D = ['E', 'J', 'S', 'Z', '3', 'L', '2', '5']
A = input()
pl = 0
B=A[::-1]
symbols = []
symb = []
for symbol in A:
    symbols += symbol
for symbol in B:
    symb += symbol
z = True
for i in range(len(symbols)):
    if (symbols[i] not in C) and (symbols[i] not in D):
        z = False
    elif symbols[i] in C:
        symbols[i] = symbols[i]
    elif symbols[i] == 'E':
        symbols[i] = '3'
    elif symbols[i] == 'J':
        symbols[i] = 'L'
    elif symbols[i] == 'S':
        symbols[i] = '2'
    elif symbols[i] == 'Z':
        symbols[i] = '5'
    elif symbols[i] == '3':
        symbols[i] = 'E'
    elif symbols[i] == 'L':
        symbols[i] = 'J'
    elif symbols[i] == '2':
        symbols[i] = 'S'
    elif symbols[i] == '5':
        symbols[i] = 'Z'
if z == False:
    arg = False
else:
    for i in range(len(symbols)):
        if symbols[i] == symb[i]:
            pl +=1
        else:
            arg = False
'''
if pl == len(A):
    print(A, 'is a mirrored string')
else:
    print(A, 'is  not a mirrored string')
'''


b = False
for i in range(len(symbols)):
    if symbols[i]==symb[i]:
        b = True
    else:
        b = False
if (b == True) and (pl == len(A)):
    print(A, 'is a mirrored palindrome.')
elif (b == True) and (pl != len(A)):
    print(A, 'is a regular palindrome.')
elif (b == False) and (pl == len(A)):
    print(A, 'is  a mirrored string.')
else:
    print(A, 'is not a palindrome.')
