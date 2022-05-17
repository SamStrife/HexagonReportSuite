supplier_spend_columns =\
    "\"Number\" as job_number,\
    \"Required\"  as job_date,\
    \"Registration\" as registration,\
    \"Vehicle Type\" as vehicle_type,\
    \"Job Type\" as job_type,\
    \"Distance\" as vehicle_mileage,\
    \"Status\" as job_status,\
    \"Supplier\" as supplier,\
    \"Customer\" as customer,\
    \"Item Description\" as job_description,\
    \"Days Vehicle Off Road\" as days_vor,\
    \"Labour\" as labour_cost,\
    \"Parts\" as parts_cost,\
    \"Cost\" as total_cost,\
    \"Recharge\" as recharge"

vehicle_details = \
    "\"Manufacturer Name\" as manufacturer,\
    \"Model Name\"  as model,\
    \"Vehicle Type Name\" as vehicleType,\
    \"Vehicle Status Name\" as status,\
    \"Vehicle Sub Status Name\" as subStatus,\
    \"Customer Name\" as customer,\
    \"Current Mileage\" as mileage,\
    \"Next Inspection Date\" as inspectionDue,\
    \"Next MOT Date\" as motDue,\
    \"Next Tacho Calibration Date\" as tachoDue,\
    \"Location\" as location"

yard_sheet = \
    "\"Unique ID\" as Vehicle_Unique_ID,\
    \"Registration\"  as Registration,\
    \"Vehicle Type Name\" as Vehicle_Type,\
    \"Vehicle Status Name\" as Vehicle_Status,\
    \"Vehicle Sub Status Name\" as Vehicle_Sub_Status,\
    \"Customer Name\" as Customer,\
    \"Current Mileage\" as Current_Mileage,\
    \"Next Inspection Date\" as Vehicle_Inspection_Due,\
    \"Next MOT Date\" as Vehicle_MOT_Due,\
    \"Next Tacho Calibration Date\" as Vehicle_Tacho_Due,\
    \"Location\" as Location,\
    \"Status Changed Date\" as Status_Date"


