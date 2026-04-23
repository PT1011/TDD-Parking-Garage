def enter_garage(garage, car_id, entry_hour):
    if len(garage['cars']) >= garage['capacity']:
        raise ValueError("Garage is full")
    
    if car_id in garage['cars'].keys():
        raise ValueError("No duplicate cars")

    garage['cars'][car_id] = entry_hour

def exit_garage(garage, car_id):
    pass

def get_available_spots(garage):
    pass

def calculate_fee(hours, rate):
    pass