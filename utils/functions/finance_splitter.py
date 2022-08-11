import pandas as pd
from utils.database import queries
from utils.database.connection import cnxn
from datetime import datetime


def report_for_agreement_splitter(dataframe):
    all_agreements = str(queries.finance_agreement_splitter_report())
    agreements = pd.read_sql(all_agreements, cnxn)
    agreements['days_open'] = agreements.apply(calculate_days_open, axis=1)
    agreements['daily_rate'] = agreements.apply(calculate_daily_rate, axis=1)
    split = calculate_revenue_split(dataframe, agreements)
    return split


def calculate_individual_agreement_costs(vehicle_id):
    all_agreements = str(queries.finance_agreement_splitter_report())
    agreements = pd.read_sql(all_agreements, cnxn)
    agreements['days_on_rent'] = agreements.apply(calculate_days_open, axis=1)
    agreements['daily_rate'] = agreements.apply(calculate_daily_rate, axis=1)
    vehicle_revenue = []
    for row in agreements.iterrows():
        vehicle_id_number = row[1].loc['vehicle_ID']
        daily_rate = row[1].loc['daily_rate']
        days_on_rent = row[1].loc['days_on_rent']
        agreement_number = row[1].loc['finance_id']
        if vehicle_id == vehicle_id_number:
            vehicle_revenue.append({agreement_number: daily_rate * days_on_rent, 'Days on rent: ': days_on_rent, 'Daily Rate: ': daily_rate})
    return vehicle_revenue


def calculate_days_open(agreement) -> int:
    start_date = agreement['finance_start_date']
    end_date = agreement['finance_end_date']

    if agreement['finance_live']:
        end_date = datetime.today()

    delta = end_date - start_date
    return delta.days


def calculate_daily_rate(hire) -> float | None:
    return round(((hire['finance_monthly_payment'] * 12) / 52) / 7, 2)


def calculate_revenue_split(dataframe, table) -> {}:
    vehicle_revenue = {}
    for vehicle in dataframe.iterrows():
        vehicle_id = vehicle[1].loc['vehicle_id']
        vehicle_revenue[vehicle_id] = {'3': 0, '12': 0, 'Life': 0}
    for row in table.iterrows():
        vehicle_id = row[1].loc['vehicle_ID']
        live = row[1].loc['finance_live']
        daily_rate = row[1].loc['daily_rate']
        days_on_rent = row[1].loc['days_open']
        hire_end = row[1].loc['finance_end_date']
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






