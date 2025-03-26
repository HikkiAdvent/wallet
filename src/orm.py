from typing import Annotated

from sqlalchemy.orm import Session
from fastapi import Depends

from src.database import sync_session


def get_session():
    with sync_session() as session:
        return session


SessionDep = Annotated[Session, Depends(get_session)]
