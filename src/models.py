from sqlalchemy import CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base, sync_engine


class Wallet(Base):
    __tablename__ = 'wallet'

    id: Mapped[int] = mapped_column(primary_key=True)
    balance: Mapped[int] = mapped_column(default=0)

    __table_args__ = (
        CheckConstraint('balance >= 0', name='balance_positive'),
    )


def create_tables() -> None:
    Base.metadata.create_all(sync_engine)


def reset_tables() -> None:
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
