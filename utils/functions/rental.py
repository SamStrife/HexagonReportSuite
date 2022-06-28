def calculate_monthly_hire_rate(rate: int, frequency: str) -> int:
    """Takes an int (rate) and string(frequency) and returns the monthly hire cost for a vehicle"""
    if frequency.lower() == "monthly":
        return int(rate)
    if frequency.lower() == "weekly":
        return int((rate*52)/12)
    if frequency.lower() != "monthly" or frequency.lower() != "weekly":
        raise TypeError("Please ensure billing frequency is set to either 'weekly' or 'monthly'")


def calculate_weekly_hire_rate(rate: int, frequency: str) -> int:
    """Takes an int (rate) and string(frequency) and returns the weekly hire cost for a vehicle"""
    if frequency.lower() == "weekly":
        return int(rate)
    if frequency.lower() == "monthly":
        return int((rate*12)/52)
    if frequency.lower() != "monthly" or frequency.lower() != "weekly":
        raise TypeError("Please ensure billing frequency is set to either 'weekly' or 'monthly'")


def calculate_daily_hire_rate(rate: int, frequency: str) -> int:
    """Takes an int (rate) and string(frequency) and returns the daily hire cost for a vehicle"""
    if frequency.lower() == "weekly":
        return int(rate/5)
    if frequency.lower() == "monthly":
        return int(((rate*12)/52)/5)
    if frequency.lower() != "monthly" or frequency.lower() != "weekly":
        raise TypeError("Please ensure billing frequency is set to either 'weekly' or 'monthly'")