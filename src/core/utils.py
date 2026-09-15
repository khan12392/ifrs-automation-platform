"""
Core utilities for the IFRS Automation Platform.
"""

from datetime import datetime
import pandas as pd


def round_currency(value, decimals=2):
    """Round a currency value to the given decimals."""
    return round(float(value), decimals)


def load_csv(filepath):
    """Load a CSV file and return a DataFrame."""
    return pd.read_csv(filepath)


def save_output(df, filepath):
    """Save a DataFrame to CSV."""
    df.to_csv(filepath, index=False)
    print(f"✅ Saved: {filepath}")


def period_label(date):
    """Return a YYYY-MM period label."""
    if isinstance(date, str):
        date = datetime.strptime(date, "%Y-%m-%d")
    return date.strftime("%Y-%m")


def format_currency(value):
    """Format a number as currency with thousands separators."""
    return f"{value:,.2f}"


def safe_divide(numerator, denominator, default=0.0):
    """Divide safely — returns default if denominator is zero."""
    if denominator == 0:
        return default
    return numerator / denominator


def calculate_present_value(payments, rate):
    """
    Calculate the present value of a series of payments.
    payments: list of (period, amount) tuples
    rate: discount rate per period (decimal)
    """
    pv = 0
    for period, amount in payments:
        pv += amount / ((1 + rate) ** period)
    return pv
