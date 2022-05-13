from utils.database import functions
import pandas as pd


supplier_spend = functions.supplier_spend(supplier="Motus", final_costs=True)
print(supplier_spend.head())
