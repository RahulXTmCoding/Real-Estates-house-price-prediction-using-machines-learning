import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__data_columns2=None
__model = None
__model2=None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)



def get_estimated_price2(bedrooms,bathrooms,sqft_lv,sqft_lot,floors,condition,grade,sqft_above,sqft_basement,lat,longg):
    

    x = np.zeros(len(__data_columns2))
    x[0] = bedrooms
    x[1] = bathrooms
    x[2] = sqft_lv
    x[3] = sqft_lot
    x[4] = floors
    x[5] = condition
    x[6] = grade
    x[7] = sqft_above
    x[8] = sqft_basement
    x[9] = lat
    x[10] = longg

    return round(__model2.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global  __data_columns2
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    with open("./artifacts/columns2.json", "r") as f:
        __data_columns2 = json.load(f)['data_columns']
        

    global __model
    global __model2
    if __model is None:
        with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

    if __model2 is None:
        with open('./artifacts/FinalModelUs.pickle','rb') as f:
            __model2=pickle.load(f)

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

def get_data_columns2():
    return __data_columns2


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price2(3 ,1.00,1180,5650,1.0,3,7,1180,0,47.5112,-122.257))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location