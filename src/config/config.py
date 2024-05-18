from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Configuración de la base de datos MySQL
DATABASE_URL = os.getenv('DATABASE_URL', 'mysql+pymysql://root:@localhost/dbname')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Importa tus modelos para que SQLAlchemy los reconozca
from models.Product import Product
from models.Order import Order

# Crea las tablas en la base de datos
Base.metadata.create_all(bind=engine)

print("Base de datos configurada y tablas creadas.")
