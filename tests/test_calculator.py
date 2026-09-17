from src.core.utils import calculate_lease_liability

def test_lease_liability_standard():
    # $10,000/year for 5 years at 5% should be $43,294.77
    result = calculate_lease_liability(10000, 5, 0.05)
    assert round(result, 2) == 43294.77

def test_lease_liability_zero_interest():
    # $10,000/year for 5 years at 0% should just be $50,000
    result = calculate_lease_liability(10000, 5, 0)
    assert result == 50000.0