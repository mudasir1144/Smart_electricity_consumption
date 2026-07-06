"""
utils.py

Utility functions used throughout the
Smart Electricity Consumption Prediction System.
"""


def calculate_monthly_consumption(daily_consumption):
    """
    Calculate monthly electricity consumption.
    """
    return round(daily_consumption * 30, 2)


def calculate_monthly_bill(monthly_consumption, rate_per_kwh=65):
    """
    Calculate estimated monthly electricity bill.

    Parameters:
        monthly_consumption (float)
        rate_per_kwh (float)

    Returns:
        Monthly bill (float)
    """

    return round(monthly_consumption * rate_per_kwh, 2)


def get_efficiency_score(daily_consumption):
    """
    Returns energy efficiency category.
    """

    if daily_consumption < 15:
        return "Excellent ⭐⭐⭐⭐⭐"

    elif daily_consumption < 25:
        return "Good ⭐⭐⭐⭐"

    elif daily_consumption < 35:
        return "Average ⭐⭐⭐"

    else:
        return "High Consumption ⭐⭐"


def format_currency(amount):
    """
    Format currency with commas.
    """

    return f"Rs. {amount:,.0f}"


def format_energy(value):
    """
    Format energy values.
    """

    return f"{value:.2f} kWh"