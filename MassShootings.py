import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

ms = pd.read_excel('MASS SHOOTINGS.xlsx')

ms.shape

ms.rename(columns = {'S#':'Caso_No.', 'Title':'Titulo', 'Location':'Lugar', 'Date':'Dia', 'civilian intervention':'Intervencion_civil', 'police intervention':'Intervencion_policial'}, inplace= True)
ms.rename(columns = {'suicide':'Suicidio', 'age.1':'Edad', 'motive':'Motivo','Summary':'Resumen', 'Fatalities':'Muertes','Injured':'Heridos','Total victims':'Victimas_Totales', 'Mental Health Issues':'Problemas_de_Salud_Mental'}, inplace= True)
ms.rename(columns = {'Race':'Raza', 'Gender':'Genero', 'Latitude':'Latitud', 'Longitude':'Longitud','STATE':'Estado','GUNCONTROL':'Control_de_armas','STRICT':'Estrictos','NOT STRICT':'No_Estrictos'}, inplace= True)


ms.drop(['age','SCHOOL', 'GANG', 'CRIME', 'ALTERCATION','POLITICAL','FAMILY', 'RANDOM','WORK', 'WELL', 'ILL', 'latino', 'native am', 'asian', 'black', 'white', 'Na', 'NaN', 'NAA', 'NAAA', 'male','female','0G', '1G', '2G', '3G', '4G', '5G', '7G', '8G', '9G', '10G'], axis=1, inplace=True)

print("La suma de la columna de las Victimas Totales es::", ms['Victimas_Totales'].sum())
print("La suma de la columna de los Suicidios es:", ms['Suicidio'].sum())
print("La media de la columna de las Victimas Totales es:", ms['Victimas_Totales'].mean())
print("La media de la columna de los Suicidios es:", ms['Suicidio'].mean())
print("La suma acumulada de la columna de las Victimas Totales es:", ms['Victimas_Totales'].cumsum())
print("La suma acumulada de la columna de los Suicidios es:", ms['Suicidio'].cumsum())
print("El resumen estadístico de la columna de las Victimas Totales es:", ms['Victimas_Totales'].describe())
print("El resumen estadístico de la columna de los Suicidios es:", ms['Suicidio'].describe())
print("La mediana de la columna de las Victimas Totales es:", ms['Victimas_Totales'].median())
print("La mediana de la columna de los Suicidios es:", ms['Suicidio'].median())
print("La varianza de la columna de las Victimas Totales es:", ms['Victimas_Totales'].var())
print("La varianza de la columna de los Suicidios es:", ms['Suicidio'].var())
print("La desviación estándar de la columna de las Victimas Totales es:", ms['Victimas_Totales'].std())
print("La desviación estándar de la columna de los Suicidios es:", ms['Suicidio'].std())

print("El promedio de víctimas totales en Estados Unidos es de:", ms['Victimas_Totales'].mean())

print(ms.corr())

Y = ms[ms['Problemas_de_Salud_Mental']=='Yes']
Y.to_csv('SI_TIENEN.csv', index=False)

#Data visualization
ms['Muertes'].value_counts().sort_index().plot.bar()
ms[ms['Victimas_Totales'] < 35]['Victimas_Totales'].plot.hist()
ms.plot.area()
sns.countplot(ms['Problemas_de_Salud_Mental'])
plt.title("Problemas de Salud Mental")
#Visualizacion con seaborn
plt.show()
sns.countplot(ms['Victimas_Totales'].head(60))
plt.show()
