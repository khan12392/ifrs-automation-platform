from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import os

from src.core.utils import calculate_lease_liability
from src.database import SessionLocal, Lease

app = FastAPI(title="IFRS Automation Platform")

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_index():
    return FileResponse(os.path.join("src", "index.html"))

@app.get("/calculate-ifrs16")
def calculate_ifrs16(name: str, lease_payment: float, years: int, discount_rate: float, db: Session = Depends(get_db)):
    # 1. Calculate the liability
    liability = calculate_lease_liability(lease_payment, years, discount_rate)
    
    # 2. Save to database
    new_lease = Lease(
        name=name,
        annual_payment=lease_payment,
        years=years,
        discount_rate=discount_rate,
        liability=round(liability, 2)
    )
    db.add(new_lease)
    db.commit()
    db.refresh(new_lease)
    
    # 3. Return the result
    return {
        "id": new_lease.id,
        "name": new_lease.name,
        "lease_liability": new_lease.liability
    }

@app.get("/leases")
def get_all_leases(db: Session = Depends(get_db)):
    return db.query(Lease).all()