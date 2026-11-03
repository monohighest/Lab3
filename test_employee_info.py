import employee_info

def test_calculate_average_salary():
    
    
    expected_avg = 361000 / 6
    result = employee_info.calculate_average_salary()
    assert result == expected_avg

def test_get_employees_by_age_range():
    
    result = employee_info.get_employees_by_age_range(22, 35)
    assert len(result) == 4

def test_get_employees_by_dept():
    
    result = employee_info.get_employees_by_dept("Marketing")
    assert len(result) == 2
    assert result[0]["name"] == "Jane"
    assert result[1]["name"] == "Mary"