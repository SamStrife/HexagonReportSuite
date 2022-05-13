from utils.database import database

test = database.get_vehicle_details(registration="DX12AEA")
print(test)