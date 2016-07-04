# perform k nearest neighbors

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split

file=pd.read_csv('File_name.csv')

#Define columns and rows 
def_features=file[['Column_Name_1','', 'Column_Name_2',''Column_Name'_3']].values 
def_target=ds.species.values
features_train,features_test,target_train,target_test=train_test_split(def_features,def_target,test_size=0.20,random_state=0)

model =KNeighborsClassifier(5).fit(features_train,target_train)
print model.predict(features_test)
print target_test
model.predict_proba(features_test)
model.score(features_test,target_test)
