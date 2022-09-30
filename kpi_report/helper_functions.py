from datetime import timedelta


def calculate_revenue_stream(vehicle):
    try:
        recharge_amount = vehicle['Recharge Amount']
        if recharge_amount > 0:
            return "Recharges"
        else:
            pass
    except KeyError:
        pass
    hire_type = vehicle['Hire Type Name']
    if hire_type == "Spot Hire":
        return "Short Term"
    elif hire_type == "Admin":
        return "Fleet Management"
    elif hire_type == "Customer own Vehicle":
        return "Fleet Management"
    elif hire_type == "Contract Hire":
        return "Contract Hire"
    elif hire_type == "Fleet Management":
        return "Fleet Management"
    elif hire_type == "Captive Sub":
        return "Short Term"
    elif hire_type == "Replacement":
        return "Short Term"
    elif hire_type == "PAYG":
        return "Short Term"
    elif hire_type == "Contract":
        return "Contract Hire"
    elif hire_type == "Cross Hire":
        return "Short Term"
    else:
        return "Undefined"


def calculate_repair_category(vehicle):
    job_type = vehicle['Job Type']
    if job_type == "Estimate":
        return "Other"
    elif job_type == "Inspection":
        return "Routine"
    elif job_type == "Repair":
        return "Other"
    elif job_type == "Tyre":
        return "Tyres"
    elif job_type == "Defect/Repairs":
        return "Breakdowns"
    elif job_type == "Breakdown":
        return "Breakdowns"
    elif job_type == "Paintwork":
        return "Other"
    elif job_type == "Parts":
        return "Other"
    elif job_type == "Service":
        return "Routine"
    elif job_type == "Maintenance":
        return "Routine"
    elif job_type == "Tachograph":
        return "Routine"
    elif job_type == "MOT":
        return "MOT"
    elif job_type == "Fridge":
        return "Routine"
    elif job_type == "Administration":
        return "Other"
    elif job_type == "Tail Lift":
        return "Routine"
    elif job_type == "Recall":
        return "Other"
    elif job_type == "Vehicle Return Work":
        return "Other"
    elif job_type == "Fuel":
        return "Other"
    elif job_type == "Hire Desk":
        return "Other"
    elif job_type == "De Hire":
        return "Other"
    elif job_type == "R&M Collection And Delivery":
        return "Other"
    elif job_type == "Brake Test":
        return "Routine"
    elif job_type == "Recovery":
        return "Breakdowns"
    else:
        return "Undefined"


def calculate_spend_amount(vehicle):
    recharge_amount = vehicle['Recharge Amount']
    cost_amount = vehicle['Internal Cost']
    if recharge_amount > 0:
        return recharge_amount
    else:
        return cost_amount


def last_day_of_month(date):
    if date.month == 12:
        return date.replace(day=31)
    return date.replace(month=date.month+1, day=1) - timedelta(days=1)