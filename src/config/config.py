# config/config.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'mysql://root@localhost/comanda_db'


engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
