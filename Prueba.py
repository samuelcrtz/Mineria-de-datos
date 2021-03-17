import pandas as pd

data = {'Nombre': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'Edad': [42, 52, 36, 24, 73], 
        'Examen_1': [80, 60, 98, 69, 80],
        'Examen_2': [78, 76, 90, 62, 80]}
df = pd.DataFrame(data, columns = ['Nombre', 'Edad', 'Examen_1', 'Examen_2'])

print(df)

df['Edad'].sum()

df['Examen_1'].mean()

df['Examen_1'].cumsum()

df['Examen_2'].describe()

df.cov()



