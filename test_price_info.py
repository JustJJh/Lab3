import price_info

# Test total_cost_shopping function
def test_total_cost_shopping():
    test_cost = 46.75
    result = price_info.total_cost_shopping()
    assert (result == test_cost)


def test_cost_of_fruits():
    price_list = {'apple': 1.20, 'orange': 1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear': 0.90, 'papaya': 2.95,'pomegranate': 4.95}
    test_cost = 12

    result = price_info.cost_of_fruits('apple',10)
    assert (result == test_cost)



