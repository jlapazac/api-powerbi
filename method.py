import pyodbc
import pandas as pd

def exec_reader(cn, query):
    try:
        cursor = cn.cursor()
        df = pd.read_sql(query, cn)
        cursor.close()
        del cursor
        cn.close()
        return df
    except Exception as error:
        print(error)

def exec_query(cn, query):
    try:
        cursor = cn.cursor()
        cursor.execute(query)
        cn.commit()
        cursor.close()
        del cursor
        cn.close()
    except Exception as error:
        print(error)

def exec_escalar(cn, query):
    try:
        cursor = cn.cursor()
        cursor.execute(query)
        if(cursor.rowcount != 0):
            row = cursor.fetchone()[0]
        else:
            row = None
        cursor.close()
        del cursor
        cn.close()

        return row
    except Exception as error:
        print(error)