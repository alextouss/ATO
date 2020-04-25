import mysql.connector
from mysql.connector import Error

list=[2098732746919692154,2119525847175343796]

try:
    connection = mysql.connector.connect(host='172.16.224.19',
                                         database='rctkoesio',
                                         user='rctkoesio',
                                         password='rdsHyibKASnw')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()

        stmt=""
        for elem in list:
            stmt = stmt +'select*from custom_properties where id={};'.format(elem)
        print(stmt)
        for result in cursor.execute(stmt,multi=True):
            if result.with_rows:
                print("Rows produced by statement '{}':".format(
                    result.statement))
                print(result.fetchall())
            else:
                print("Number of rows affected by statement '{}': {}".format(
                    result.statement, result.rowcount))

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
