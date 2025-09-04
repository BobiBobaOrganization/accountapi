from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

class Account(BaseModel):
    id: UUID                 = Field(default_factory=uuid4)
    userid: UUID             = Field(default_factory=uuid4)
    username: str            = Field(..., min_length=5, max_length=20)
    firstname: Optional[str] = Field(None, max_length=256)
    lastname: Optional[str]  = Field(None, max_length=256)
    sex: Optional[str]       = Field(None, max_length=24)
    phone: Optional[str]     = Field(None, max_length=16)
    
class AccountPut(BaseModel):
    username: Optional[str]  = Field(None, min_length=5, max_length=20)
    firstname: Optional[str] = Field(None, max_length=256)
    lastname: Optional[str]  = Field(None, max_length=256)
    sex: Optional[str]       = Field(None, max_length=24)
    phone: Optional[str]     = Field(None, max_length=16)