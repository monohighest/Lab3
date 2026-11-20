import price_info


def test_total_cost_shopping():
    #Arrange
    expected_total = 46.75
    #Act
    result = price_info.total_cost_shopping()
    #Assert
    assert result == expected_total


def test_cost_of_fruits():
    # Arrange
    fruit_name = 'apple'
    quantity = 10
    expected_result = 12.0

    # Act
    result = price_info.cost_of_fruits(fruit_name, quantity)

    # Assert
    assert result == expected_result