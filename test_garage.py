import pytest
from garage import enter_garage, exit_garage

def test_enter_garage_works():
    garage_dict = {
    "capacity": 10,   # total number of spots
    "cars": {}         # car_id -> entry_hour (int)
    }
    enter_garage(garage_dict, 'Bugatti17', 13)
    assert 'Bugatti17' in garage_dict['cars'].keys()

def test_enter_garage_full():
    with pytest.raises(ValueError):
        garage_dict = {
        "capacity": 1,   # total number of spots
        "cars": {'Toyota': 14}         # car_id -> entry_hour (int)
        }
        enter_garage(garage_dict, 'Bugatti17', 13)

def test_enter_garage_car_exists():
    with pytest.raises(ValueError):
        garage_dict = {
        "capacity": 2,   # total number of spots
        "cars": {'Toyota': 14}         # car_id -> entry_hour (int)
        }
        enter_garage(garage_dict, 'Toyota', 14)
        
def test_enter_garage_car_time_not_int():
    with pytest.raises(TypeError):
        garage_dict = {
        "capacity": 10,   # total number of spots
        "cars": {}         # car_id -> entry_hour (int)
        }
        enter_garage(garage_dict, 'Bugatti12', 'fourteen')

def test_exit_garage_works():
    garage_dict = {
        "capacity": 10,   # total number of spots
        "cars": {'Toyota': 14}         # car_id -> entry_hour (int)
        }
    exit_garage(garage_dict, 'Toyota')
    assert 'Toyota' garage_dict['cars'].keys()