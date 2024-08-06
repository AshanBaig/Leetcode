import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

db=pd.read_csv('data.csv')
db
# %matplotlib inline
plt.xlabel('Area(sq ft)')
plt.ylabel('Price(&US)')
plt.scatter(db.area,db.price,color='red',marker='+')
# plt.show()