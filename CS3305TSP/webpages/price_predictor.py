
#Takes values from forms and assigns to relevant variables

city = 0
county = 0
floor_plan = 0
property_type = 0
number_of_bedrooms = 0
number_of_bathrooms = 0
energy_rating = 0
size = 0

coef1 = 12202.62557933
coef2 = -809.74017648
coef3 = 773.86062167
coef4 = -58114.19523757
coef5 = 8324.17775815

intercept = 220759.72278872645

# average expected price rise of homes = 4%
# average increase per month


def predict(values):
    """

    :param values: an array of fields such as rooms, bathrooms ect
    :return: an estimate pricing
    """
    val1 = values[0][0] * coef1
    val2 = values[0][1] * coef2
    val3 = values[0][2] * coef3
    val4 = values[0][3] * coef4
    val5 = values[0][4] * coef5
    price = val1+val2+val3+val4+val5+intercept
    price = int(round(price, 0))

    return price


def predict_future_price(price):
    """
    :param price: takes in an estimated prices by the matrices above
    :return: an array of estimated prices
    """
    price_array = []
    for x in range(12):
        x += 1
        y = ((1.04) ** (x / 12))
        p = int(round((price * y), 0))
        price_array.append(p)
    return price_array

