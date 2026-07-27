from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data_models import Base

engine = create_engine("sqlite:///Homeworks/Homework20/students.db", echo=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()