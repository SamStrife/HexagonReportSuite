import pandas as pd
from utils.database import queries
from utils.database.connection import cnxn


def derby_yard_sheet():
    data = pd.read_sql(queries.derby_yard_sheet, cnxn)
    vehicles_marked_at_derby = data[data["Location"].str.contains("Derby", na=False)]
    vehicles_marked_at_derby = vehicles_marked_at_derby[vehicles_marked_at_derby["Vehicle_Status"] != "No longer on fleet"]
    vehicles_marked_at_derby["Yard_Sheet_Date"] = pd.to_datetime('today')
    vehicles_marked_at_derby["Vehicle_ID_Date_Identifier"] = vehicles_marked_at_derby.apply(vehicle_ID_date_identifier, axis=1)
    vehicles_marked_at_derby["ID"] = vehicles_marked_at_derby.apply(id_generator, axis=1)
    vehicles_marked_at_derby.set_index("ID", inplace=True)
    return vehicles_marked_at_derby


def id_generator(vehicle):
    return f"{int(vehicle['Vehicle_Unique_ID'])}{vehicle['Yard_Sheet_Date'].strftime('%d%m%Y')}{vehicle['Status_Date'].strftime('%d%m%Y')}"


def vehicle_ID_date_identifier(vehicle):
    return f"{int(vehicle['Vehicle_Unique_ID'])}{vehicle['Status_Date'].strftime('%d%m%Y')}"
