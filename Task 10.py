sogl = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'ь','ъ', 'м', 'н', 'п', 'р', 'с', 'т', 'ф','х','ц','ч','ш', 'щ']
glas = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
with open('dz.txt', 'r', encoding="utf-8") as infile1:
    L1 = infile1.read()
A = L1.split()
j = 0
Spisokbukv = list(map(list, A))
for i in range(len(Spisokbukv)):
    d= len(Spisokbukv[i])
    while j < d:
        if Spisokbukv[i][j] in glas:
            if j!=0:
                if Spisokbukv[i][j-1] in sogl:
                    Spisokbukv[i].insert(j+1, 'с' + Spisokbukv[i][j])
                    d += 1

        j+=1
    j =0
print(Spisokbukv)
Z = [''.join(map(str, inner_spisok)) for inner_spisok in Spisokbukv]
print(Z)
fin = ' '.join(Z)
print(fin)

