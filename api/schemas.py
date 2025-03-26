from pydantic import BaseModel
from enum import Enum


class OperationType(str, Enum):
    DEPOSIT = 'DEPOSIT'
    WITHDRAW = 'WITHDRAW'


class OperationRequest(BaseModel):
    operation_type: OperationType
    amount: int
