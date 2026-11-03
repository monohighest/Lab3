import Lab2.bmi as bmi

def test_bmi_normal_weight():
    # Test calculate_bmi returning 0 for normal weight
    result = bmi.calculate_bmi(height=1.73, weight=65)
    assert result == 0

def test_bmi_over_weight():
    # Test calculate_bmi returning 1 for overweight
    result = bmi.calculate_bmi(height=1.73, weight=85)
    assert result == 1

def test_bmi_under_weight():
    # Test calculate_bmi returning -1 for underweight
    result = bmi.calculate_bmi(height=1.73, weight=45)
    assert result == -1