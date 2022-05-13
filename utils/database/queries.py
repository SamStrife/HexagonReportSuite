from utils.database import database

vehicle_query = f"Select * from {database['vehicles']};"
purchase_order_query = f"Select * from {database['purchaseOrders']};"
job_query = f"Select * from {database['jobs']};",
hire_query = f"Select * from {database['hires']};"

