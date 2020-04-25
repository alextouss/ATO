import sqlalchemy as db

""" https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91 """

engine = db.create_engine('mysql+mysqlconnector://rctkoesio:rdsHyibKASnw@172.16.224.19/rctkoesio')
connection = engine.connect()

metadata = db.MetaData()
census = db.Table('guarantee', metadata, autoload=True, autoload_with=engine)
print(census.columns.keys())