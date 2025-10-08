import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv("C:/Users/user/Downloads/BTC_data.csv")
x = df['time']
x_p = x[::25]
y = df['close']
plt.plot(x,y)
print(x)
print(x_p)
plt.xticks(x_p, rotation=90)
plt.subplots_adjust(bottom=0.27)
plt.grid(True)
plt.show()
plt.savefig('Task_5_graph.png', dpi=500)
print(df)
