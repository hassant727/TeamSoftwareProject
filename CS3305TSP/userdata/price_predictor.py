import pickle
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model



#Takes values from forms and assigns to relevant variables

city = 0
county = 0
floor_plan = 0
property_type = 0
number_of_bedrooms = 0
number_of_bathrooms = 0
energy_rating = 0
size = 0

predict = "price"

# values = [[city ,county, property_type ,number_of_bedrooms ,number_of_bathrooms ,energy_rating, size]]
# to be filled in by values given by the user

values = [[4, 2, 139, 2, 9]]

y = np.array([])


pickle_in = open("HousingModel.pickle", "rb")
linear = pickle.load(pickle_in)

def predict(values):
    predictions = linear.predict(values)
    print(predictions)
    return predictions

