from utils.database import column_selectors as cs
from utils.database import databases as db

# Generic Queries
vehicle_query = f"Select * from {db.vehicles};"
purchase_order_query = f"Select * from {db.purchase_orders};"
job_query = f"Select * from {db.jobs};",
hire_query = f"Select * from {db.hires};"

# More Specific Queries
supplier_spend = f"Select {cs.supplier_spend_columns} from {db.jobs};"