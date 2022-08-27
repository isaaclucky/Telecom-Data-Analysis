import os
import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error


def DBConnect(dbName=None):

    conn = mysql.connect(host='localhost', user='owon', password='lucky1Z_',
                         database=dbName, buffered=True)
    cur = conn.cursor()
    return conn, cur




def createDB(dbName: str) -> None:

    conn, cur = DBConnect()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
    conn.commit()
    cur.close()


def createTables(dbName: str) -> None:

    conn, cur = DBConnect(dbName)
    sqlFile = 'schema.sql'
    fd = open(sqlFile, 'r')
    readSqlFile = fd.read()
    fd.close()

    sqlCommands = readSqlFile.split(';')

    for command in sqlCommands:
        try:
            res = cur.execute(command)
        except Exception as ex:
            print("Command skipped: ", command)
            print(ex)
    conn.commit()
    cur.close()

    return



def insert_to_telecom_table(dbName: str, df: pd.DataFrame, table_name: str) -> None:
    
    conn, cur = DBConnect(dbName)

    for _, row in df.iterrows():
        sqlQuery = f"""INSERT INTO {table_name}(User_ID,Experience_score,Engagement_score,Satisfaction_score)  
        VALUES(%s,%s,%s,%s)"""
        data = (row[0], row[1], row[2], row[3])

        try:
            # Execute the SQL command
            cur.execute(sqlQuery, data)
            # Commit your changes in the database
            conn.commit()
            print("Data Inserted Successfully")
        except Exception as e:
            conn.rollback()
            print("Error: ", e)
    return


def db_execute_fetch(*args, many=False, tablename='', rdf=True, **kwargs) -> pd.DataFrame:
    
    connection, cursor1 = DBConnect(**kwargs)
    if many:
        cursor1.executemany(*args)
    else:
        cursor1.execute(*args)

    # get column names
    field_names = [i[0] for i in cursor1.description]

    # get column values
    res = cursor1.fetchall()

    # get row count and show info
    nrow = cursor1.rowcount
    if tablename:
        print(f"{nrow} recrods fetched from {tablename} table")

    cursor1.close()
    connection.close()

    # return result
    if rdf:
        return pd.DataFrame(res, columns=field_names)
    else:
        return res


if __name__ == "__main__":
    
    createTables(dbName='Telecom')
    df = pd.read_pickle('../data/df_sat_final.pkl')
    insert_to_telecom_table(dbName='Telecom', df=df,
                          table_name='Customer_Satisfaction')
