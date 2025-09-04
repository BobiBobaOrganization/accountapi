from abc import ABC, abstractmethod
from typing import Optional
from sqlalchemy import UUID

from src.models.account import Account, AccountPut

class AccountStorage(ABC):
    @abstractmethod
    def get_account_id(self, account_id: UUID) -> Optional[Account]:
        pass
    @abstractmethod
    def get_account_username(self, username) -> Optional[Account]:
        pass
    @abstractmethod
    def update_account(self, account_id: UUID, updated_account: AccountPut) -> Optional[Account]:
        pass