import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
df=pd.read_csv("student-math.csv")
df['final grade']=df['G1'] + df['G2'] + df['G3']
df.drop(['G1'],['G2'],['G3'],axis=1,inplace=True)
df.replace({
    'Yes':1,
    'No':0
})
area=np.pi*3
plt.scatter(df["studytime"],df["finalgrade"],c=green,s=area,alpha=0.5)
plt.xlabel("studytime")
plt.ylabel("finalgrade")
plt.show()
