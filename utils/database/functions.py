import pandas as pd
from utils.database import queries
from utils.database import connection


def test():
    return pd.read_sql(queries.supplier_spend, connection.cnxn)
