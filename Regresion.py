import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
from matplotlib import pyplot as plt

ms = pd.read_excel('MASS SHOOTINGS2.xlsx')

ms.rename(columns = {'S#':'Caso_No.', 'Title':'Titulo', \
'Location':'Lugar', 'Date':'Dia', 'civilian intervention':'Intervencion_civil',\
     'police intervention':'Intervencion_policial'}, inplace= True)
ms.rename(columns = {'suicide':'Suicidio', 'age.1':'Edad', 'motive':'Motivo','Summary':'Resumen', 'Fatalities':'Muertes','Injured':'Heridos','Total victims':'Victimas_Totales', 'Mental Health Issues':'Problemas_de_Salud_Mental'}, inplace= True)
ms.rename(columns = {'Race':'Raza', 'Gender':'Genero', 'Latitude':'Latitud', 'Longitude':'Longitud','STATE':'Estado','GUNCONTROL':'Control_de_armas','STRICT':'Estrictos','NOT STRICT':'No_Estrictos'}, inplace= True)

#Eliminando columnas que no necesito
ms.drop(['age','SCHOOL', 'GANG', 'CRIME', 'ALTERCATION','POLITICAL','FAMILY', 'RANDOM','WORK', 'WELL', 'ILL', 'latino', 'native am', 'asian', 'black', 'white', 'Na', 'NaN', 'NAA', 'NAAA', 'male','female','0G', '1G', '2G', '3G', '4G', '5G', '7G', '8G', '9G', '10G'], axis=1, inplace=True)


datos_x = ms['Muertes']
datos_y = ms['Heridos']

plt.scatter(x=datos_x , y=datos_y, marker='o', c='black', s=5)
plt.title("Gráfico de puntos y estimación de la recta de regresión simple")
plt.xlabel("Muertes")
plt.ylabel("Heridos")
plt.show()

array_x = np.array(ms['Muertes'])
array_y = np.array(ms['Heridos'])

n = len(array_x)
sum_x = sum(array_x)
sum_y = sum(array_y)
sum_xy = sum(array_x*array_y)
sum_xx = sum(array_x*array_x)

s_xy = sum_xy-(1/n)*sum_x*sum_y
s_xx = sum_xx-(1/n)*sum_x**2

beta_1 = s_xy / s_xx
beta_0 = (1/n)*sum_y - beta_1*(1/n)*sum_x

print("La estimación de los parámetros para el modelo de regresión son: ")
print("beta1: ",(beta_1))
print("beta0: ",(beta_0))

plt.scatter(x=datos_x , y=datos_y, marker='o', c='black', s=5)
plt.plot(array_x, beta_0 + beta_1 * array_x, '-', c='red')
plt.title("Gráfico de puntos y estimación de la recta de regresión simple")
plt.xlabel("Muertes")
plt.ylabel("Heridos")
plt.show()