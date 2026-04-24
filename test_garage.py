import pytest
from garage import enter_garage, exit_garage, get_available_spots, calculate_fee

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
    assert 'Toyota' not in garage_dict['cars'].keys()

def test_exit_garage_car_doesnt_exist():
    with pytest.raises(KeyError):
        garage_dict = {
        "capacity": 10,   # total number of spots
        "cars": {'Toyota12': 14}         # car_id -> entry_hour (int)
        }
        exit_garage(garage_dict, 'Toyota')

def test_get_available_spots_works():
    garage_dict = {
        "capacity": 10,   # total number of spots
        "cars": {'Toyota12': 14}         # car_id -> entry_hour (int)
        }

    assert get_available_spots(garage_dict) == 9

def test_get_available_spots_garage_is_full():
    garage_dict = {
        "capacity": 1,   # total number of spots
        "cars": {'Toyota12': 14}         # car_id -> entry_hour (int)
        }
    
    assert get_available_spots(garage_dict) == 0

@pytest.mark.parametrize("hours, rate, expected",[(3, 2, 6.00), (11, 2, 22.00), (10, 0.2, 2.00)])
def test_calculate_fee_multiple_test(hours, rate, expected):
    assert calculate_fee(hours, rate) == expected

@pytest.mark.parametrize("hours, rate",[(-3, 2), (11, -2)])
def test_calculate_fee_multiple_test(hours, rate):
    with pytest.raises(ValueError) 
        calculate_fee(hours, rate)
