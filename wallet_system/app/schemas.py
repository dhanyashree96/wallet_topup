from pydantic import BaseModel

class WalletBase(BaseModel):
    user_id: str

class WalletCreate(WalletBase):
    pass

class WalletUpdate(WalletBase):
    amount: float

class Wallet(WalletBase):
    balance: float

    class Config:
        orm_mode = True
