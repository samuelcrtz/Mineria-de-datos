from sklearn import datasets
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

ventas = pd.read_csv("ventas2.csv")
objetivo = "monto"
independientes = ventas.drop(columns=['monto']).columns

modelo = LinearRegression()
modelo.fit(X=ventas[independientes], y=ventas[objetivo])

ventas["ventas_prediccion"] = modelo.predict(ventas[independientes])
preds = ventas[["monto", "ventas_prediccion"]].head(50)

talvez = modelo.predict([[41,1,1,1]])
print ("Tal vez compre: ")
print (talvez)

preds.plot(kind='bar',figsize=(18,8))
plt.grid(linewidth='2')
plt.grid(linewidth='2')
plt.grid(None)
plt.show()