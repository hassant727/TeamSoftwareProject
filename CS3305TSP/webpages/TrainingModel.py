#import tensorflow
#import keras
#import pandas as pd
#import numpy as np
#import sklearn
#from sklearn import linear_model
#from sklearn.utils import shuffle

# Anaconda enviroment needs to be set up to run code

#data = pd.read_csv("HousingData.csv", sep=";")

#data = data[["Training fields"]]

#predict = "Price"

#x = np.array(data.drop([predict], 1))
#y = np.array(data[predict])

#x_train, x_test, y_train,  y_test = sklearn.model_selection.train_test_split(x, y, test_size= 0.1 )

#linear = linear_model.LinearRegression()

#linear.fit(x_train, y_train)

#acc = linear.score(x_test, y_test)
#print(acc)

#print("Co: ",'\n', linear.coef_)
#print("Intercept:", '\n', linear.intercept_)

#predict price
#predictions = linear.predict(x_test)

#for x in range(len(predictions)):
    #print(predictions[x], x_test[x], y_test[x])