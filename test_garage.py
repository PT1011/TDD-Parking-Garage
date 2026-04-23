import pytest
from garage import enter_garage

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
        enter(garage_dict, 'Bugatti17', 13)
        