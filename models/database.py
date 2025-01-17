from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Column()
Integer()
String()
ForeignKey()
declarative_base()
sessionmaker()
relationship()

# Database setup
Base = declarative_base()
engine = create_engine('sqlite:///data/rpg.db')
Session = sessionmaker(bind=engine)

def init_db():
    # *** Initialize my db ***
    Base.metadata.create_all(engine)