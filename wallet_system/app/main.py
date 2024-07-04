from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/topup", response_model=schemas.Wallet)
def top_up(wallet: schemas.WalletUpdate, db: Session = Depends(get_db)):
    db_wallet = crud.top_up_wallet(db, wallet.user_id, wallet.amount)
    if db_wallet is None:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return db_wallet

@app.post("/deduct", response_model=schemas.Wallet)
def deduct(wallet: schemas.WalletUpdate, db: Session = Depends(get_db)):
    db_wallet = crud.deduct_wallet(db, wallet.user_id, wallet.amount)
    if db_wallet is None:
        raise HTTPException(status_code=404, detail="Wallet not found or insufficient balance")
    return db_wallet

@app.get("/balance", response_model=schemas.Wallet)
def get_balance(user_id: str, db: Session = Depends(get_db)):
    db_wallet = crud.get_wallet(db, user_id)
    if db_wallet is None:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return db_wallet
