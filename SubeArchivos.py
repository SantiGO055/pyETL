import pandas as pd
import os
from modules.config import data_path
import pyodbc
import numpy as np

connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL SERVER}; SERVER=DESKTOP-P6L04G8\SQLEXPRESS;DATABASE=Archivos;Trusted_Connection=yes')

cursor = connection.cursor()
# cursor.execute("SELECT * FROM TablaArchivo")
# for i in cursor:
#     print(i)


# cursor.execute(f'INSERT INTO TablaArchivo ({ID}, product_name, price)'
#                'VALUES'
#                "(5,'Chair',120),"
#                "(6,'Tablet',300)"
#                '')
# connection.commit()


filename = os.path.join(data_path(), 'age_income.csv')
data = pd.read_csv(filename)
df = pd.DataFrame(data)
# print(df)
df2 = df.replace(np.nan,'',regex=True)
for row in df2.itertuples():
    print(row.MaritalStatus)
    cursor.execute('''
    INSERT INTO TablaArchivo (ID, Name,MaritalStatus,Age,Income)
    VALUES (?,?,?,?,?)
    ''',
                   row.Index,
                   row.Name,
                   row.MaritalStatus,
                   int(row.Age),
                   int(row.Income))

connection.commit()

cursor.close()
connection.close()
# print(df)
