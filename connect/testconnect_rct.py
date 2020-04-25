import mysql.connector as db

# store the connection object in the variable cnx
cnx = db.connect(host='172.16.224.19', database='rctkoesio',user='rctkoesio',password='rdsHyibKASnw')

# create a new cursor, by default a MySQLCursor object, using the connection's cursor() method
cursor= cnx.cursor()

#execute the operation stored in the query variable using the execute() method
query="select * from guarantee where compte_id = 25"
cursor.execute(query)
result = cursor.fetchall()
print(cursor.column_names)
