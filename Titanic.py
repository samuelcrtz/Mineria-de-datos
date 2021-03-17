import pandas
import numpy as np
import matplotlib.pyplot as plt

input_file = 'titanic_data.csv'
separador = ","
dataset = pandas.read_csv(filepath_or_buffer=input_file, sep=separador)

df1 = pandas.DataFrame(np.random.randn(6,4),index=list(range(0,12,2)),columns=list(range(10,18,2)))

def gender_number(gender):
    if gender == 'male': return 0.
    return 1.

def age_ranges(x):
    return '[{0}-{1})'.format(10*int(x/10), 10 +10*int(x/10))

print (df1)
print (dataset.Sex.unique())
print ("El numero de filas y columnas que incluye el dataset es: ",dataset.shape)
print ("\nLos nombres de las columnas son: \n",dataset.columns)
print ("\nLa primera fila del dataset es: \n",dataset.head(1))
print ("\nLa última fila del dataset es: \n",dataset.tail(1))