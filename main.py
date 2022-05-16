from utils.functions import functions

test = functions.derby_yard_sheet()
print("Vehicles at Derby")
print(test['vehicles_marked_at_derby'])
print("Vehicles Outside Derby")
print(test['vehicles_outside_of_derby'])

