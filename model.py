import pandas as pd
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
df= pd.read_excel('finalsheet1final.xlsx')
X=df[['Material','Test type','Tool diameter','Spindle speed','Step depth','Feed rate']]
y=df['Formability']
X = pd.get_dummies(X, columns=['Material', 'Test type'])
print(X.head(2))
model = LinearRegression()
model.fit(X,df['Formability'])
pickle.dump(model, open('model3.pkl','wb'))
