from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select, update

from api.schemas import OperationType, OperationRequest
from src.models import Wallet
from src.orm import SessionDep

router = APIRouter(prefix='/api/v1/wallets')


@router.get('/')
def get_all(session: SessionDep):
    return session.query(Wallet).all()


@router.post('/')
def create(session: SessionDep, status_code=status.HTTP_201_CREATED):
    wallet = Wallet()
    session.add(wallet)
    session.commit()
    session.refresh(wallet)
    return {'message': 'wallet is created', 'id': wallet.id}


@router.get(path='/{wallet_id}')
def get_balance(wallet_id: int, session: SessionDep):
    wallet = session.query(Wallet).filter(Wallet.id == wallet_id).first()
    if wallet:
        return {'balance': wallet.balance}
    raise HTTPException(status_code=404, detail='Wallet not found')


@router.delete('/{wallet_id}')
def delete_wallet_endpoint(wallet_id: int, session: SessionDep):
    wallet = session.query(Wallet).filter(Wallet.id == wallet_id).first()
    if wallet:
        session.delete(wallet)
        session.commit()
        return {'message': 'Wallet deleted'}
    raise HTTPException(status_code=404, detail='Wallet not found')


@router.post(path='/{wallet_id}/operation')
def performe_operation(
    wallet_id: int,
    operation: OperationRequest,
    session: SessionDep
):
    with session.begin():
        wallet = session.execute(
            select(Wallet).filter(Wallet.id == wallet_id).with_for_update()
        ).scalar_one_or_none()

        if not wallet:
            raise HTTPException(status_code=404, detail='Wallet not found')

        if operation.operation_type == OperationType.DEPOSIT:
            wallet.balance += operation.amount
        elif operation.operation_type == OperationType.WITHDRAW:
            if wallet.balance >= operation.amount:
                wallet.balance -= operation.amount
            else:
                raise HTTPException(
                    status_code=400,
                    detail='Insufficient funds'
                )
        session.execute(
            update(Wallet).where(Wallet.id == wallet_id)
            .values(balance=wallet.balance)
        )

    return {
        'message': 'Operation successful',
        'balance': wallet.balance
    }