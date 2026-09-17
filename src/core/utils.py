def calculate_lease_liability(annual_payment: float, years: int, discount_rate: float) -> float:
    """
    Calculate the present value of future lease payments (IFRS 16).
    Formula: PV = PMT * [(1 - (1 + r)^-n) / r]
    """
    if discount_rate == 0:
        return annual_payment * years
    
    # Present Value of an Annuity formula
    pv = annual_payment * ((1 - (1 + discount_rate) ** -years) / discount_rate)
    return pv