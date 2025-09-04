from typing import Optional

from sqlalchemy import UUID
from src.db.entities import AccountTable
from sqlalchemy.orm import Session
from src.services.account_storage import AccountStorage
from src.models.account import Account, AccountPut

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = getattr(row, column.name)
    return d

class AccountRepository(AccountStorage):
    def __init__(self, db: Session):
        self.db = db

    def get_account_id(self, account_id: UUID) -> Optional[Account]:
        account = self.db.query(AccountTable).filter(AccountTable.id == account_id).first()
        if account:
            return Account(**row2dict(account))
        return None
    
    def get_account_username(self, username) -> Optional[Account]:
        account = self.db.query(AccountTable).filter(AccountTable.username == username).first()
        if account:
            return Account(**row2dict(account))
        return None
    
    def update_account(self, account_id: UUID, updated_account: AccountPut) -> Optional[Account]:
        account = self.db.query(AccountTable).filter(AccountTable.id == account_id).first()
        if account:
            for field, value in updated_account.model_dump(exclude_unset=True).items():
                setattr(account, field, value)
            self.db.commit()
            return Account(**row2dict(account))
        return None