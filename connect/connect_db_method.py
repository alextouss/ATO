import mysql.connector as db
from credentials import host, database,user, password
import json

class connect_db:

    def __init__(self):
        self.conn = db.connect(host=host, database=database,user=user, password=password)
        self.cursor = self.conn.cursor()

    def __del__(self):
        # body of destructor
        self.conn.close()

    def execute_query(self,query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def col_names(self,query):
        self.cursor.execute(query)
        cols_name = self.cursor.column_names
        return cols_name

query="SELECT * from guarantee"
first_conn=connect_db()
my_result = first_conn.execute_query(query)
my_cols=first_conn.col_names(query)


my_data = [dict(zip(my_cols,gar_values)) for gar_values in my_result]
print(my_data)