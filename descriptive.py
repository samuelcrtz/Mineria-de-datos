import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import matplotlib.pyplot as plt

ms = pd.read_excel('MASS SHOOTINGS.xlsx')

ms.drop(['age','SCHOOL','GANG','CRIME','ALTERCATION','POLITICAL','FAMILY','RANDOM','WORK','latino','native am','asian','black','white','Na','NaN','NAA','NAAA','male','female','0G','1G','2G','3G','4G','5G','7G','8G','9G','10G','police intervention','civilian intervention','Latitude','Longitude'], axis=1, inplace=True)

ms.rename(columns = {'S#':'Caso_No.'}, inplace= True)
ms.rename(columns = {'Title':'Titulo'}, inplace= True)
ms.rename(columns = {'Location':'Lugar'}, inplace= True)
ms.rename(columns = {'Date':'Dia'}, inplace= True)
ms.rename(columns = {'civilian intervention':'Intervencion_civil'}, inplace= True)
ms.rename(columns = {'police intervention':'Intervencion_policial'}, inplace= True)
ms.rename(columns = {'suicide':'Suicidio'}, inplace= True)
ms.rename(columns = {'age.1':'Edad'}, inplace= True)
ms.rename(columns = {'motive':'Motivo'}, inplace= True)
ms.rename(columns = {'Summary':'Resumen'}, inplace= True)
ms.rename(columns = {'Fatalities':'Muertes'}, inplace= True)
ms.rename(columns = {'Injured':'Heridos'}, inplace= True)
ms.rename(columns = {'Total victims':'Victimas_Totales'}, inplace= True)
ms.rename(columns = {'Mental Health Issues':'Problemas_de_Salud_Mental'}, inplace= True)
ms.rename(columns = {'Race':'Raza'}, inplace= True)
ms.rename(columns = {'Gender':'Genero'}, inplace= True)
ms.rename(columns = {'Latitude':'Latitud'}, inplace= True)
ms.rename(columns = {'Longitude':'Longitud'}, inplace= True)
ms.rename(columns = {'STATE':'Estado'}, inplace= True)
ms.rename(columns = {'GUNCONTROL':'Control_de_armas'}, inplace= True)
ms.rename(columns = {'STRICT':'Estrictos'}, inplace= True)
ms.rename(columns = {'NOT STRICT':'No_Estrictos'}, inplace= True)
ms.rename(columns = {'WELL':'Sanos'}, inplace= True)
ms.rename(columns = {'ILL':'Enfermos'}, inplace= True)

#Estadistica descriptiva

print("\n\nEstadisticas del CSV")
print(ms.describe())
print(ms.columns)
print(ms.dtypes)
print(ms.index)

print("\n\nEstadisticas Columna Total de Victimas")
print(ms['Victimas_Totales'].describe())
print(ms['Victimas_Totales'].dtypes)
print(ms['Victimas_Totales'].index)

print("\n\nEstadisticas Columna Suicidos")
print(ms['Suicidio'].describe())
print(ms['Suicidio'].dtypes)
print(ms['Suicidio'].index)

print("\n\nEstadisticas Columna Muertes")
print(ms['Muertes'].describe())
print(ms['Muertes'].dtypes)
print(ms['Muertes'].index)

print("\n\nEstadisticas Columna Sanos")
print(ms['Sanos'].describe())
print(ms['Sanos'].dtypes)
print(ms['Sanos'].index)

print("\n\nEstadisticas Columna Enfermos")
print(ms['Enfermos'].describe())
print(ms['Enfermos'].dtypes)
print(ms['Enfermos'].index)

