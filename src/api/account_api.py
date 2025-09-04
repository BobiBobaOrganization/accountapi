from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from src.dependencies import get_account_storage
from src.models.account import Account, AccountPut

from src.services.account_storage import AccountStorage

router = APIRouter()

@router.get("/accounts/i/{account_id}", response_model=Account)
def get_account_id(account_id: UUID, service: AccountStorage = Depends(get_account_storage)) -> Optional[Account]:
    """
    Get account by ID.
    """
    account = service.get_account_id(account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

@router.get("/accounts/u/{username}", response_model=Account)
def get_account_username(username: str, service: AccountStorage = Depends(get_account_storage)) -> Optional[Account]:
    """
    Get account by username.
    """
    account = service.get_account_username(username)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

@router.put("/accounts/{account_id}", response_model=Account)
def update_account(account_id: UUID, updated_account: AccountPut, service: AccountStorage = Depends(get_account_storage)) -> Optional[Account]:
    """
    Update account by ID.
    """
    account = service.update_account(account_id, updated_account)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

