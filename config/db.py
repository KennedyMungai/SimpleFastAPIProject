from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://root@localhost:3306/sql_alchemy_intro")

conn = engine.connect()
