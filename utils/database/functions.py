import pandas as pd
from utils.database import queries
from utils.database.connection import cnxn


def supplier_spend(supplier=None, final_costs=False, styling=None):
    data = pd.read_sql(queries.supplier_spend, cnxn, index_col="job_number")
    if supplier:
        data = data[data['supplier'].str.contains(supplier, na=False)]
    if final_costs:
        data = data[data['job_status'] == 'Complete']
    if styling:
        pass
    return data
