from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config import get_settings
from src.db.account_repository import AccountRepository
from src.services.account_service import AccountService
from src.services.account_storage import AccountStorage

def get_account_storage() -> AccountStorage:
    if get_settings().TEST_MODE:
        return AccountService() 
    else:
        engine = create_engine(get_settings().DATABASE_URL, echo=True)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        return AccountRepository(db)





    