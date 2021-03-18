import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

ms = pd.read_excel('MASS SHOOTINGS.xlsx')

ms.shape

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

ms.drop(['age','SCHOOL', 'GANG', 'CRIME', 'ALTERCATION','POLITICAL','FAMILY', 'RANDOM','WORK', 'WELL', 'ILL', 'latino', 'native am', 'asian', 'black', 'white', 'Na', 'NaN', 'NAA', 'NAAA', 'male','female','0G', '1G', '2G', '3G', '4G', '5G', '7G', '8G', '9G', '10G'], axis=1, inplace=True)

print("La suma de la columna de las Victimas Totales es::", ms['Victimas_Totales'].sum())
print("La suma de la columna de los Suicidios es:", ms['Suicidio'].sum())
print("La media de la columna de las Victimas Totales es:", ms['Victimas_Totales'].mean())
print("La media de la columna de los Suicidios es:", ms['Suicidio'].mean())
