import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df= pd.read_csv("iris.csv")
# print(df.values)
(train_set, test_set) = train_test_split(df.values, train_size= 0.7, random_state= 40582)

train_inputs = train_set[:,0:4]
train_classes = train_set[:,4]

print(train_inputs)
print(train_classes)

test_inputs = test_set[:,0:4]
test_classes = test_set[:,4]

dt = DecisionTreeClassifier()

dt.fit(train_inputs, train_classes)
print(dt.score(test_inputs,test_classes))
