import pyodbc

def str_ds_pejcb933bdrp_Latam():
  try:
    cn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=localhost;DATABASE=Azure;UID=sa;PWD=Konecta++123')
  except Exception as identifier:
    cn = None
  
  return cn
 
def str_dt_pejcb933bdrp_Latam():
  try:
    cn = 'mssql+pyodbc://sa_Latam:54_L4T4M_2018@pejcb933bdrp:1433/Latam?driver=ODBC Driver 17 for SQL Server'
  except Exception as error:
    cn = None
  
  return cn