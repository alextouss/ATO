import mysql.connector as db
from credentials import host, database,user, password

# store the connection object in the variable cnx
cnx = db.connect(host=host, database=database,user=user, password=password)

# create a new cursor, by default a MySQLCursor object, using the connection's cursor() method
cursor= cnx.cursor()

#execute the operation stored in the query variable using the execute() method
query="select * from guarantee"
cursor.execute(query)
result = cursor.fetchall()
print(cursor.column_names)
print(result)
