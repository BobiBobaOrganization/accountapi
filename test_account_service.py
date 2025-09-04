from uuid import UUID
import pytest
from uuid import uuid4
from src.models.account import AccountPut
from src.services.account_service import AccountService

@pytest.fixture
def account_service():
    return AccountService()
def test_get_account_id(account_service):
    account = account_service.get_account_username("test_user1")
    retrieved_account = account_service.get_account_id(account.id)
    assert retrieved_account is not None
    assert retrieved_account.username == "test_user1"
def test_get_account_id_not_found(account_service):
    non_existent_id = uuid4()
    retrieved_account = account_service.get_account_id(non_existent_id)
    assert retrieved_account is None
def test_get_account_username(account_service):
    account = account_service.get_account_username("test_user2")
    assert account is not None
    assert account.username == "test_user2"
def test_get_account_username_not_found(account_service):
    account = account_service.get_account_username("non_existent_user")
    assert account is None
def test_update_account(account_service):
    account = account_service.get_account_username("test_user1")
    updated_data = AccountPut(username="updated_user1")
    updated_account = account_service.update_account(account.id, updated_data)
    assert updated_account is not None
    assert updated_account.username == "updated_user1"
def test_update_account_not_found(account_service):
    non_existent_id = uuid4()
    updated_data = AccountPut(username="non_existent_user")
    updated_account = account_service.update_account(non_existent_id, updated_data)
    assert updated_account is None