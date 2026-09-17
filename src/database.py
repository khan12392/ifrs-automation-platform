from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.orm import declarative_base, sessionmaker

# This creates a file called "ifrs_data.db" in your project folder
SQLALCHEMY_DATABASE_URL = "sqlite:///./ifrs_data.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Lease(Base):
    __tablename__ = "leases"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    annual_payment = Column(Float)
    years = Column(Integer)
    discount_rate = Column(Float)
    liability = Column(Float)

# Create the tables
Base.metadata.create_all(bind=engine)