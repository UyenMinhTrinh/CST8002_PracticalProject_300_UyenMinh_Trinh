from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Create SQLite Database
DATABASE_URL = "sqlite:///data.db"
engine = create_engine(DATABASE_URL, echo=True)  # Set echo=False to hide SQL logs

# Base class for ORM models
Base = declarative_base()

# Create Session
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Define a Table Model
class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)

# Create the Table
Base.metadata.create_all(engine)

print("Database setup complete!")
