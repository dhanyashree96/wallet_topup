from sqlalchemy.orm import Session
from .models import Wallet

def get_wallet(db: Session, user_id: str):
    return db.query(Wallet).filter(Wallet.user_id == user_id).first()

def create_wallet(db: Session, user_id: str):
    db_wallet = Wallet(user_id=user_id)
    db.add(db_wallet)
    db.commit()
    db.refresh(db_wallet)
    return db_wallet

def top_up_wallet(db: Session, user_id: str, amount: float):
    wallet = get_wallet(db, user_id)
    if wallet:
        wallet.balance += amount
        db.commit()
        db.refresh(wallet)
    return wallet

def deduct_wallet(db: Session, user_id: str, amount: float):
    wallet = get_wallet(db, user_id)
    if wallet and wallet.balance >= amount:
        wallet.balance -= amount
        db.commit()
        db.refresh(wallet)
    return wallet
