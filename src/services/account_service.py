import logging
from uuid import UUID
from typing import Optional

from src.models.account import Account, AccountPut
from src.services.account_storage import AccountStorage

class AccountService(AccountStorage):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AccountService, cls).__new__(cls)
            cls._instance.accounts = []
            cls._instance.initialize_test_data()
        return cls._instance

    def get_account_id(self, account_id: UUID) -> Optional[Account]:
        for account in self.accounts:
            if account.id == account_id:
                return account
        return None
    
    def get_account_username(self, username) -> Optional[Account]:
        for account in self.accounts:
            if account.username == username:
                return account
        return None
    
    def update_account(self, account_id: UUID, updated_account: AccountPut) -> Optional[Account]:
        for account in self.accounts:
            if account.id == account_id:
                for field, value in updated_account.model_dump(exclude_unset=True).items():
                    setattr(account, field, value)
                return account
        return None
    
    def initialize_test_data(self):
        test_users = [
            {"username": "test_user1"},
            {"username": "test_user2"},
        ]
        for user_data in test_users:
            logging.info("Account created: %s" % user_data)
            self.accounts.append(Account(**user_data))