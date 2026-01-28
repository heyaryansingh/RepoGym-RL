from math_utils import calculate_average

def test_average():
    assert calculate_average([1, 2, 3]) == 2.0
    assert calculate_average([10, 20]) == 15.0
    assert calculate_average([]) == 0
