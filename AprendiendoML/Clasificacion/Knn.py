"""
    En clasificacion elige al que tiene más miembros
    de vecinos cercanos y lo asigna como tal
"""

#Set de Datos de Flores
from sklearn.datasets import load_iris
# Dividir datos en set de entrenamiento y test
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
print(iris.keys())

xTrain, xTest, yTrain, yTest = train_test_split(iris['data'],iris['target'])
print("Flores y sus menciones",xTrain.shape)
print("Etiquetas correspondientes a x",yTrain.shape)

knn = KNeighborsClassifier(n_neighbors=7)
#Entrenar
knn.fit(xTrain,yTrain)

print("Precision: ",knn.score(xTest,yTest))

#Predecir ingresando medidas: #knn.predict([[1,2,3,4]])
print(iris.target_names[knn.predict([[12,2,3,4]])])
