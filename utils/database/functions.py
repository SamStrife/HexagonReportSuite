import pandas as pd
from utils.database import queries
from utils.database.connection import cnxn


def test():
    return pd.read_sql(queries.supplier_spend, cnxn)
