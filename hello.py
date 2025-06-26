import numpy as np
import pandas as pd
import pickle


#loading the saved model
loader_model = pickle.load(open('D:/Streamlit Project/model/car_price_prediction_model.sav', 'rb'))

# input_data = (2013,70000,1,1,1,0)  # example: Diesel=1, Dealer=1, Automatic=1, First Owner=0
input_data = (2017,150000,0,0,0,0)  # example: year=2017,km=150000,petrol=0, Dealer=0, Manual=0, First Owner=0


input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loader_model.predict(input_data_reshaped)

print("Predicted Price :",prediction,"Rupees")


# Optional: Compare to some threshold if needed
threshold = 100000  # 1 lakh
if prediction > threshold:
  print('Sell')
else:
  print('Not Sell')
