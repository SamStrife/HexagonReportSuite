import pandas as pd
from utils.database import queries
from utils.database.connection import cnxn
from datetime import datetime


def report_for_hire_splitter():
    all_hires = str(queries.hires_for_splitter_report())
    hires = pd.read_sql(all_hires, cnxn)
    hires['days_on_rent'] = hires.apply(calculate_days_on_rent, axis=1)
    hires['daily_rate'] = hires.apply(calculate_daily_rate, axis=1)
    split = calculate_revenue_split(hires)
    return split


def calculate_individual_vehicle_rental_revenues(vehicle_id):
    all_hires = str(queries.hires_for_splitter_report())
    hires = pd.read_sql(all_hires, cnxn)
    hires['days_on_rent'] = hires.apply(calculate_days_on_rent, axis=1)
    hires['daily_rate'] = hires.apply(calculate_daily_rate, axis=1)

    vehicle_revenue = []
    for row in hires.iterrows():
        vehicle_id_number = row[1].loc['vehicle_ID']
        daily_rate = row[1].loc['daily_rate']
        days_on_rent = row[1].loc['days_on_rent']
        agreement_number = row[1].loc['agreement_number']
        if vehicle_id == vehicle_id_number:
            vehicle_revenue.append({agreement_number: daily_rate * days_on_rent})
    return vehicle_revenue


def calculate_days_on_rent(hire) -> int:
    start_date = hire['hire_start']
    end_date = hire['hire_end']

    if hire['live']:
        end_date = datetime.today()

    delta = end_date - start_date
    return delta.days


def calculate_daily_rate(hire) -> float | None:
    if hire['frequency'] == "Weekly":
        return round(hire['sales'] / 5, 2)
    elif hire['frequency'] == "Monthly":
        return round(((hire['sales'] * 12) / 52) / 5, 2)
    elif hire['frequency'] == 'Daily':
        return round(hire['sales'], 2)
    else:
        return None


def calculate_revenue_split(table) -> {}:
    vehicle_revenue = {}
    for row in table.iterrows():
        vehicle_id = row[1].loc['vehicle_ID']
        live = row[1].loc['live']
        daily_rate = row[1].loc['daily_rate']
        days_on_rent = row[1].loc['days_on_rent']
        hire_end = row[1].loc['hire_end']
        if vehicle_id not in vehicle_revenue.keys():
            vehicle_revenue[vehicle_id] = {'3': 0, '12': 0, 'Life': 0}
        if live:
            vehicle_revenue[vehicle_id]['3'] += round(daily_rate * min(91, days_on_rent), 2)
            vehicle_revenue[vehicle_id]['12'] += round(daily_rate * min(365, days_on_rent), 2)
            vehicle_revenue[vehicle_id]['Life'] += round(daily_rate * days_on_rent, 2)
        else:
            days_since_rent_end = (datetime.today() - hire_end).days
            if days_since_rent_end > 365:
                vehicle_revenue[vehicle_id]['Life'] += round(daily_rate * days_on_rent, 2)
            elif 91 < days_since_rent_end <= 365:
                vehicle_revenue[vehicle_id]['Life'] += round(daily_rate * days_on_rent, 2)
                vehicle_revenue[vehicle_id]['12'] += round(daily_rate * min(365 - days_since_rent_end, days_on_rent), 2)
            elif days_since_rent_end <= 91:
                vehicle_revenue[vehicle_id]['Life'] += round(daily_rate * days_on_rent, 2)
                vehicle_revenue[vehicle_id]['12'] += round(daily_rate * min(365 - days_since_rent_end, days_on_rent), 2)
                vehicle_revenue[vehicle_id]['3'] += round(daily_rate * min(91 - days_since_rent_end, days_on_rent), 2)
            else:
                pass
    return vehicle_revenue






