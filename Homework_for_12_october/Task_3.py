import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
Iris_serosa = 0
Iris_virginica = 0
Iris_versicolor = 0
L_12 = 0
L_1215 = 0
L_15 = 0
df = pd.read_csv("C:/Users/user/Downloads/iris_data.csv")
for i in range(len(df['Species'])):
    if df['Species'][i] == 'Iris-setosa':
        Iris_serosa+=1
    elif df['Species'][i] == 'Iris-virginica':
        Iris_virginica+=1
    elif df['Species'][i] == 'Iris-versicolor':
        Iris_versicolor+=1
print(Iris_serosa, Iris_virginica, Iris_versicolor)

dol1 = (Iris_serosa/len(df['Species']))*100

dol2 = (Iris_virginica/len(df['Species']))*100
dol3 = (Iris_versicolor/len(df['Species']))*100
fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax1.pie([Iris_serosa, Iris_virginica, Iris_versicolor], labels=['Iris serosa', 'Iris virginica', 'Iris versicolor'])
ax1.legend([str(round(dol1, 2))+'%',str(round(dol2, 2))+'%',str(round(dol3, 2))+'%'],loc='lower left')
#print(df['PetalWidthCm'])
for i in range(len(df['PetalLengthCm'])):
    if df['PetalLengthCm'][i] < 1.2:
        L_12 +=1
    elif df['PetalLengthCm'][i] > 1.5:
        L_15 +=1
    elif (df['PetalLengthCm'][i] >= 1.2) and (df['PetalLengthCm'][i] <= 1.5):
        L_1215 +=1
print(L_12, L_1215, L_15)
dol_c_12 = (L_12/len(df['PetalLengthCm']))*100
dol_c_15 = (L_15/len(df['PetalLengthCm']))*100
dol_c_1215 = (L_1215/len(df['PetalLengthCm']))*100
ax2.pie([L_12, L_1215, L_15], labels=['Длина < 1,2 см', 'Длина от 1,2 см до 1,5 см', 'Длина > 1,5 см'])
ax2.legend([str(round(dol_c_12, 2))+'%',str(round(dol_c_1215, 2))+'%',str(round(dol_c_15, 2))+'%'],loc='lower right')
plt.savefig('Task_3_graph.png', dpi=300)
plt.show()