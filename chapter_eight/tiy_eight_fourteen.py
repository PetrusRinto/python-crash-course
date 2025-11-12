# Patrick 11.11.2025.
# 8-14 Cars.

def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing information about a car"""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info
