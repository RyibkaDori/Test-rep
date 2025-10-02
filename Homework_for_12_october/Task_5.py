import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv("C:/Users/user/Downloads/BTC_data.csv")
x = df['time']
y = df['close']
plt.plot(x,y)
plt.show()
plt.savefig('Task_5_graph.png', dpi=500)
print(df)