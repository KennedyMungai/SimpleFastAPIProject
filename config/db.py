"""
This is the database configuration file
"""
from sqlalchemy import create_engine, MetaData


engine = create_engine("mysql+pymysql://root@localhost:3306/sql_alchemy_intro")
meta = MetaData()
conn = engine.connect()
