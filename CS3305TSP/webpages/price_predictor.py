
#Takes values from forms and assigns to relevant variables

city = 0
county = 0
floor_plan = 0
property_type = 0
number_of_bedrooms = 0
number_of_bathrooms = 0
energy_rating = 0
size = 0


x = [[4 ,2 ,139 ,2 ,9]]

coef1 = 12202.62557933
coef2 = -809.74017648
coef3 = 773.86062167
coef4 = -58114.19523757
coef5 = 8324.17775815

intercept = 220759.72278872645

def predict(values):
    val1 = values[0][0] * coef1
    val2 = values[0][1] * coef2
    val3 = values[0][2] * coef3
    val4 = values[0][3] * coef4
    val5 = values[0][4] * coef5
    price = val1+val2+val3+val4+val5+intercept
    price = int(round(price, 0))
    print(price)
