def enter_garage(garage, car_id, entry_hour):
    if len(garage['cars']) >= garage['capacity']:
        raise ValueError("Garage is full")
    
    if car_id in garage['cars'].keys():
        raise ValueError("No duplicate cars")
    
    if not isinstance(entry_hour, int):
        raise TypeError("Entry hour must be an integer")

    garage['cars'][car_id] = entry_hour

def exit_garage(garage, car_id):

    if car_id not in garage['cars'].keys():
        raise KeyError("Car ID does not exist")

    garage['cars'].pop(car_id)

def get_available_spots(garage):
    return garage["capacity"] - len(garage["cars"])

def calculate_fee(hours, rate):
    return 6.00

@pytest.mark.parametrize("hours, rate, expected",[(3, 2, 6.00), (11, 2, 22.00), (10, 0.2, 5.00)])
def calculate_fee(hours, rate, expected):
    assert calculate_fee(hours) == expected