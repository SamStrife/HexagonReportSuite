import datetime

from utils.database.queries import vehicles_on_fleet
from utils.database.connection import cnxn
import pandas as pd
import requests
import time


def vehicles():
    df = pd.read_sql(str(vehicles_on_fleet()), cnxn)
    df['GOV MOT Date'] = df.apply(check_gov_mot_date, axis=1)
    return df


def check_gov_mot_date(vehicle):
    headers = {
        "Accept": 'application/json+v7',
        "x-api-key": 'U6662lcQWt9m6Wn3DDHIq2bKEBDW5DQ6TYzYS2y1',
    }
    try:
        response = requests.get(f"https://beta.check-mot.service.gov.uk/trade/vehicles/annual-tests?registrationsOrVins={vehicle['Registration']}", headers=headers)
        gov_mot_date = response.json()[0]['annualTestExpiryDate']
        time.sleep(0.5)
        return gov_mot_date
    except:
        try:
            headers2 = {
                "Accept": 'application/json',
                "x-api-key": 'yUsZtDSKcD4o1pjLzVzKZ8Sx1J0BzP8y8q5DVOua',
            }
            url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
            post_obj = {"registrationNumber": f"{vehicle['Registration']}"}
            response = requests.post(url, json=post_obj, headers=headers2)
            gov_mot_date = response.json()['motExpiryDate']
            return datetime.datetime.strptime(gov_mot_date, '%Y-%m-%d')
        except:
            pass
