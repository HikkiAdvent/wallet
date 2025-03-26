import pytest # noqa
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_wallet_response_format():
    response = client.post('/api/v1/wallets/')
    assert response.status_code == 200
    assert 'message' in response.json()
    assert 'id' in response.json()
    assert isinstance(response.json()['id'], int)


def test_get_all_wallets_response_format():
    response = client.get('/api/v1/wallets/')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    for wallet in response.json():
        assert 'id' in wallet
        assert 'balance' in wallet
        assert isinstance(wallet['id'], int)
        assert isinstance(wallet['balance'], int)


def test_get_balance_response_format():
    response = client.get('/api/v1/wallets/1')
    assert response.status_code == 200
    assert 'balance' in response.json()
    assert isinstance(response.json()['balance'], int)


def test_performe_operation_response_format():
    response = client.post(
        '/api/v1/wallets/1/operation',
        json={'operation_type': 'DEPOSIT', 'amount': 100}
    )
    assert response.status_code == 200
    assert 'message' in response.json()
    assert 'balance' in response.json()
    assert isinstance(response.json()['balance'], int)
