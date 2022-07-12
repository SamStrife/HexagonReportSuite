from utils.database import databases as db

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
    \"Manufacturer Name\" as Vehicle_Make,\
    \"Model Name\" as Vehicle_Model,\
    \"Vehicle Status Name\" as Vehicle_Status,\
    \"Vehicle Sub Status Name\" as Vehicle_Sub_Status,\
    \"Customer Name\" as Customer,\
    \"Current Mileage\" as Current_Mileage,\
    \"Next Inspection Date\" as Vehicle_Inspection_Due,\
    \"Next MOT Date\" as Vehicle_MOT_Due,\
    \"Next Tacho Calibration Date\" as Vehicle_Tacho_Due,\
    \"Location\" as Location,\
    \"Status Changed Date\" as Status_Date"

asset_file_vehs_and_hires_and_customers = \
    f"{db.vehicles}.[Customer Name] as customer_name,\
    {db.vehicles}.[Relationship Manager] as relationship_manager,\
    {db.vehicles}.[Vehicle Type Name] as vehicle_type,\
    {db.vehicles}.[Registration] as registration,\
    {db.vehicles}.[Hire Expiry Date] as hire_expiry_date,\
    {db.vehicles}.[Customer Account Number] as customer_acc_number,\
    {db.vehicles}.[Vehicle On Fleet Date] as vehicle_on_fleet_date,\
    {db.vehicles}.[Manufacturer Name] as manufacturer,\
    {db.vehicles}.[Model Name] as model,\
    {db.vehicles}.[Current Mileage] as mileage,\
    {db.vehicles}.[Date Mileage Taken] as mileage_date,\
    {db.vehicles}.[Annual Mileage] as contract_annual_mileage,\
    {db.vehicles}.[Financer Name] as financer, \
    {db.vehicles}.[Residual Value] as residual_value, \
    {db.vehicles}.[Hire Start Date] as hire_start_date, \
    {db.vehicles}.[Sales] as sales, \
    {db.vehicles}.[Billing Frequency Name] as billing_frequency, \
    {db.vehicles}.[Customer Unique ID] as customer_ID, \
    {db.vehicles}.[Hire Unique ID] as hire_ID, \
    {db.vehicles}.[Finance Agreement Number] as finance_agreement_number, \
    {db.customers}.[Account Status Name] as account_status, \
    {db.customers}.[Organisation Group Name] as customer_group, \
    {db.hires}.[Supplier Name] as supplier_name, \
    {db.hires}.[Supplier Unique ID] as supplier_ID, \
    {db.hires}.[Live] as live_hire"

asset_file_hires = \
    f"{db.hires}.[Supplier Name] as supplier_name, \
    {db.hires}.[Supplier Unique ID] as supplier_ID, \
    {db.hires}.[Live] as live_hire" \

asset_file_addresses = \
    f"{db.postal_addresses}.[Organisation Unique ID] as organisation_ID, \
    {db.postal_addresses}.[Postal Code] as post_code, \
    {db.postal_addresses}.[Postal Address Type Name] as address_type" \

asset_file_finance = \
    f"{db.finance}.[Monthly Depreciation] as monthly_depreciation, \
    {db.finance}.[Net Book Value] as net_book_value, \
    {db.finance}.[Finance End Date] as finance_end_date, \
    {db.finance}.[Live] as finance_live"
