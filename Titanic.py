import pandas

input_file = 'titanic_data.csv'
separador = ","
dataset = pandas.read_csv(filepath_or_buffer=input_file, sep=separador)

print ("El numero de filas y columnas que incluye el dataset es: ",dataset.shape)
print ("\nLos nombres de las columnas son: \n",dataset.columns)
print ("\nLa primera fila del dataset es: \n",dataset.head(1))
print ("\nLa última fila del dataset es: \n",dataset.tail(1))

