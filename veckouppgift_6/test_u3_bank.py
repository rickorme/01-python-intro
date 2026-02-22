
import pytest
from u3_bank import BankAccount



@pytest.mark.parametrize("initial, expected", [
    (50, 50),    # Positive balance
    (0, 0),      # Zero balance (default-like)
    (-200, -200) # Negative balance
])
def test_get_balance(initial, expected):
    account = BankAccount(initial)
    assert account.get_balance() == expected

@pytest.mark.parametrize("amount, error_msg", [
    (0, "must be positive"),
    (-1, "must be positive"),
    (None, "must have a value"),
    ("", "must be a number"),
    ("abc", "must be a number")
])
def test_deposit_errors(amount, error_msg):
    account = BankAccount()
    with pytest.raises(ValueError, match=error_msg):
        account.deposit(amount)

@pytest.mark.parametrize("initial, deposit_amount, expected_balance", [
    (100, 40, 140),   # Partial withdrawal
    (100, 100, 200),   # Exact balance (empty account)
    (50, 0.01, 50.01) # Floating point/small amount
])
def test_deposit_success(initial, deposit_amount, expected_balance):
    account = BankAccount(initial)
    account.deposit(deposit_amount)
    assert account.get_balance() == expected_balance

@pytest.mark.parametrize("amount, error_msg", [
    (0, "must be positive"),
    (-1, "must be positive"),
    (101, "Insufficient funds"),
    (None, "must have a value"),
    ("", "must be a number"),
    ("abc", "must be a number")
])
def test_withdraw_errors(amount, error_msg):
    account = BankAccount(100)
    with pytest.raises(ValueError, match=error_msg):
        account.withdraw(amount)  

@pytest.mark.parametrize("initial, withdraw_amount, expected_balance", [
    (100, 40, 60),   # Partial withdrawal
    (100, 100, 0),   # Exact balance (empty account)
    (50, 0.01, 49.99) # Floating point/small amount
])
def test_withdraw_success(initial, withdraw_amount, expected_balance):
    # Setup
    account = BankAccount(initial)
    
    # Action
    result = account.withdraw(withdraw_amount)
    
    # Assertions
    assert result == expected_balance, "The returned balance should match expected"
    assert account.get_balance() == expected_balance, "The internal state should be updated"

@pytest.mark.parametrize("interest_rate, error_msg", [
    (-0.01, "cannot be negative"),
    ("0.05", "must be a number"),
    (None, "must have a value")
])
def test_apply_interest_errors(interest_rate, error_msg):
    account = BankAccount(100, interest_rate)
    with pytest.raises(ValueError, match=error_msg):
        account.apply_interest()

@pytest.mark.parametrize("initial, interest_rate, expected_balance", [
    (100, None, 102),   # Default rate (0.02)
    (200, 0.1, 220)    # Higher interest
])
def test_apply_interest_success(initial, interest_rate, expected_balance):
    if interest_rate is None:
        account = BankAccount(initial)
    else:
        account = BankAccount(initial, interest_rate)
    account.apply_interest()
    assert account.get_balance() == expected_balance

@pytest.mark.parametrize("bill_amount, error_msg", [
    (-0.01, "cannot be negative"),
    ("0.05", "must be a number"),
    (None, "must have a value")
])
def test_can_pay_bill_errors(bill_amount, error_msg):
    account = BankAccount(100, bill_amount)
    with pytest.raises(ValueError, match=error_msg):
        account.can_pay_bill(bill_amount)

@pytest.mark.parametrize("initial, bill_amount, expected", [
    (100, 50, True),   # Can pay
    (100, 100, True),  # Can pay exact amount
    (100, 150, False)  # Cannot pay
])
def test_can_pay_bill_success(initial, bill_amount, expected):
    account = BankAccount(initial)
    result = account.can_pay_bill(bill_amount)
    assert result == expected        