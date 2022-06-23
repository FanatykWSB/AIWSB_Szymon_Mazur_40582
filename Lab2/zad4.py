import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
df= pd.read_csv("iris.csv")
# print(df.values)
(train_set, test_set) = train_test_split(df.values, train_size= 0.7, random_state= 40582)


train_inputs = train_set[:,0:4]
train_classes = train_set[:,4]
test_inputs = test_set[:,0:4]
test_classes = test_set[:,4]

knn = KNeighborsClassifier(n_neighbors=1, metric='euclidean')
knn.fit(train_inputs,train_classes)
print("dla 1: ",knn.score(test_inputs,test_classes))

knnthree = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
knnthree.fit(train_inputs,train_classes)
print("dla 3: ",knnthree.score(test_inputs,test_classes))

knnfive = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
knnfive.fit(train_inputs,train_classes)
print("dla 5: ",knnfive.score(test_inputs,test_classes))

knneleven = KNeighborsClassifier(n_neighbors=11, metric='euclidean')
knneleven.fit(train_inputs,train_classes)
print("dla 11: ",knneleven.score(test_inputs,test_classes))
