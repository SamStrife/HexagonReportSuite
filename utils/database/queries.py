from utils.database import column_selectors as cs
from utils.database import databases as db
from pypika import MSSQLQuery, Table
import pendulum

# Generic Queries
vehicle_query = f"Select * from {db.vehicles};"
purchase_order_query = f"Select * from {db.purchase_orders};"
job_query = f"Select * from {db.jobs};",
hire_query = f"Select * from {db.hires};"
supplier_query = f"Select * from {db.suppliers};"

# More Specific Queries
supplier_spend = f"Select {cs.supplier_spend_columns} from {db.jobs};"
derby_yard_sheet = f"Select {cs.yard_sheet} from {db.vehicles};"

# Asset File Queries
af_vehicles = Table(db.vehicles)
af_hires = Table(db.hires)
af_customers = Table(db.customers)
af_addresses = Table(db.postal_addresses)
af_finance = Table(db.finance)

af_vehicle_and_hire_and_customer_query = \
    MSSQLQuery\
    .from_(af_vehicles)\
    .left_join(af_hires)\
    .on(af_vehicles['Hire Unique ID'] == af_hires['Unique ID'])\
    .left_join(af_customers)\
    .on(af_vehicles['Customer Unique ID'] == af_customers['Unique ID'])\
    .select(
        af_vehicles['Unique ID'].as_('vehicle_id'),
        af_vehicles['Customer Name'].as_('customer_name'),
        af_vehicles['Relationship Manager'].as_('relationship_manager'),
        af_vehicles['Vehicle Type Name'].as_('vehicle_type'),
        af_vehicles['Parent Vehicle Type Name'].as_('parent_type'),
        af_vehicles['Registration'].as_('registration'),
        af_vehicles['Hire Expiry Date'].as_('hire_expiry_date'),
        af_vehicles['Customer Account Number'].as_('customer_acc_number'),
        af_vehicles['Vehicle On Fleet Date'].as_('vehicle_on_fleet_date'),
        af_vehicles['Manufacturer Name'].as_('manufacturer'),
        af_vehicles['Model Name'].as_('model'),
        af_vehicles['Current Mileage'].as_('mileage'),
        af_vehicles['Date Mileage Taken'].as_('mileage_date'),
        af_vehicles['Annual Mileage'].as_('contract_annual_mileage'),
        af_vehicles['Financer Name'].as_('financer'),
        af_vehicles['Residual Value'].as_('residual_value'),
        af_vehicles['Hire Start Date'].as_('hire_start_date'),
        af_vehicles['Sales'].as_('sales'),
        af_vehicles['Billing Frequency Name'].as_('billing_frequency'),
        af_vehicles['Customer Unique ID'].as_('customer_ID'),
        af_vehicles['Hire Unique ID'].as_('hire_ID'),
        af_vehicles['Finance Agreement Number'].as_('finance_agreement_number'),
        af_vehicles['Last Finance Unique ID'].as_('last_finance_unique_id'),
        af_customers['Account Status Name'].as_('account_status'),
        af_customers['Organisation Group Name'].as_('customer_group'),
        af_hires['Supplier Name'].as_('supplier_name'),
        af_hires['Supplier Unique ID'].as_('supplier_ID'),
        af_hires['Live'].as_('live_hire'),
        af_hires['Start Mileage'].as_('hire_start_mileage'),
        af_hires['Original Hire Date'].as_('original_hire_date'),
        af_hires['Original Start Mileage'].as_('original_hire_mileage')
        )

af_finance_query = \
    MSSQLQuery\
    .from_(af_finance)\
    .select(
        af_finance['Unique ID'].as_('finance_id'),
        af_finance['Agreement Number'].as_('finance_agreement_number'),
        af_finance['Monthly Depreciation'].as_('monthly_depreciation'),
        af_finance['Net Book Value'].as_('net_book_value'),
        af_finance['Finance End Date'].as_('finance_end_date'),
        af_finance['Live'].as_('finance_live')
    )\
    .where(af_finance['Live'] == 'TRUE')\

af_address_query = \
    MSSQLQuery\
    .from_(af_addresses)\
    .select(
        af_addresses['Organisation Unique ID'].as_('organisation_ID'),
        af_addresses['Postal Code'].as_('supplier_post_code'),
    )\
    .where(af_addresses['Postal Address Type Name'] == 'Operating')


# Vehicle Spend Queries
jobs = Table(db.jobs)
def vehicle_spend_query(vehicle, from_date, to_date):
    from_date = pendulum.from_format(from_date, 'DD/MM/YYYY').format('YYYYMMDD')
    to_date = pendulum.from_format(to_date, 'DD/MM/YYYY').format('YYYYMMDD')
    data = MSSQLQuery.from_(jobs)\
    .select('*')\
    .where(jobs['Status'] == 'Complete')\
    .where(jobs['Vehicle Unique ID'] == vehicle)\
    .where(jobs['Required'] >= from_date)\
    .where(jobs['Required'] <= to_date)
    return data

def all_spend_split():
    data = MSSQLQuery.from_(jobs)\
    .select(
    jobs['Vehicle Unique ID'].as_('vehicle_id'),
    jobs['Required'].as_('job_date'),
    jobs['Cost'].as_('cost')
    )\
    .where(jobs['Status'] == 'Complete')
    return data

