from fastapi.testclient import TestClient
from uuid import uuid4
from src.dependencies import get_account_storage
from src.services.account_storage import AccountStorage
from src.api.account_api import router
from src.models.account import Account
from fastapi import FastAPI, Depends

app = FastAPI()
app.include_router(router)

client = TestClient(app)

class MockAccountStorage:
    def __init__(self):
        self.accounts = []

    def get_account_id(self, account_id):
        for account in self.accounts:
            if account.id == account_id:
                return account
        return None

    def get_account_username(self, username):
        for account in self.accounts:
            if account.username == username:
                return account
        return None

    def update_account(self, account_id, updated_account):
        for account in self.accounts:
            if account.id == account_id:
                if updated_account.username:
                    account.username = updated_account.username
                return account
        return None

mock_storage = MockAccountStorage()

def override_get_account_storage():
    return mock_storage

app.dependency_overrides[get_account_storage] = override_get_account_storage

account_id = uuid4()
user_id = uuid4()
mock_storage.accounts.append(Account(id=account_id, userid=user_id, username="testuser"))


def test_get_account_id():    
    response = client.get(f"/accounts/i/{account_id}")
    assert response.status_code == 200
    assert response.json() == {"id": str(account_id), "userid": str(user_id), "username": "testuser", 'firstname': None, 'lastname': None, 'sex': None, 'phone': None}

def test_get_account_id_not_found():
    response = client.get(f"/accounts/i/{uuid4()}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Account not found"}

def test_get_account_username():
    response = client.get("/accounts/u/testuser")
    assert response.status_code == 200
    assert response.json() == {"id": str(account_id), "userid": str(user_id), "username": "testuser", 'firstname': None, 'lastname': None, 'sex': None, 'phone': None}

def test_get_account_username_not_found():
    response = client.get("/accounts/u/nonexistentuser")
    assert response.status_code == 404
    assert response.json() == {"detail": "Account not found"}

def test_update_account():
    updated_account = {"username": "updateduser"}
    response = client.put(f"/accounts/{account_id}", json=updated_account)
    assert response.status_code == 200
    assert response.json() == {"id": str(account_id), "userid": str(user_id), "username": "updateduser", 'firstname': None, 'lastname': None, 'sex': None, 'phone': None}

def test_update_account_not_found():
    updated_account = {"username": "updateduser"}
    response = client.put(f"/accounts/{uuid4()}", json=updated_account)
    assert response.status_code == 404
    assert response.json() == {"detail": "Account not found"}