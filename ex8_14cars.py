car_make_model = {}

def car_info(manufacturer_name, model_name, **car_data):
    
    car_make_model['manufacturer'] = manufacturer_name
    car_make_model['model'] = model_name

    for key,value in car_data.items():
        car_make_model[key] = value

    return car_make_model

car = car_info('subaru', 'outback', color = 'blue', tow_package = True)
print(car)