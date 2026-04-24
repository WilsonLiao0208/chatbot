import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def customer_data(df):
    x = []
    y = []
    z = []
    for i, row in df.iterrows():
        acc_num = int(row["ppgLength"])
        x += map(float, row["PPG2"].split(",", maxsplit = acc_num)[:-1])
        y += map(float, row["ACC_X"].split(",", maxsplit = acc_num)[:-1])
        z += map(float, row["ACC_Y"].split(",", maxsplit = acc_num)[:-1])
    return np.array([x,y,z])
df = pd.read_csv("C:/Users/samli/Desktop/python_test/test.csv")
ACC_data = customer_data(df)
plt.figure(figsize = (20,10))
plt.plot(ACC_data[0], label = 'PPG2')
plt.plot(ACC_data[1], label = 'ACC_Y')
plt.plot(ACC_data[2], label = 'ACC_Z')
plt.legend()
plt.show()