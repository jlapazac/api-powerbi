import time
import pandas as pd
import pyodbc


def set_table(source,query):
df = pd.read_csv("C:\\your_path\\CSV1.csv")

conn_str = (
    r'DRIVER={SQL Server Native Client 11.0};'
    r'SERVER=localhost;'
    r'DATABASE=Azure;'
    r'Trusted_Connection=yes;'
)
cnxn = pyodbc.connect(conn_str)

cursor = cnxn.cursor()

for index,row in df.iterrows():
    cursor.execute('INSERT INTO dbo.Table_1([Name],[Address],[Age],[Work]) values (?,?,?,?)', 
                    row['Name'], 
                    row['Address'], 
                    row['Age'],
                    row['Work'])
    cnxn.commit()
cursor.close()
cnxn.close()

# see total time to do insert
print("%s seconds ---" % (time.time() - start_time))