import pandas as pd
import matplotlib.pyplot as plt    
    

data = pd.read_csv('DOT 7_D422CD006274_20240702_111432.csv', skiprows=7)
x = data['Acc_X']
y = data['Acc_Y']
z = data['Acc_Z']

plt.figure()
plt.plot(x)
plt.plot(y)
plt.plot(z)
plt.show()
# print(data)
