import numpy as np 
import pickle
import streamlit as st


#loading the saved model
loader_model = pickle.load(open('D:/Streamlit Project/model/car_price_prediction_model.sav', 'rb'))

def car_price_prediction(input_data):
    
    # input_data = (2013,70000,1,1,1,0)  # example: Diesel=1, Dealer=1, Automatic=1, First Owner=0
    # input_data = (2017,150000,0,0,0,0)  # example: year=2017,km=150000,petrol=0, Dealer=0, Manual=0, First Owner=0


    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loader_model.predict(input_data_reshaped)
    price = prediction[0]  # Just the single value
    print("Predicted Price :",prediction,"Rupees")

# Optional: Compare to some threshold if needed
    threshold = 100000  # 1 lakh
    if prediction > threshold:
        return price,'Sell'
    else:
        return price,'dont Sell'

# year	selling_price	km_driven	fuel	seller_type	transmission	owner

def main():

    st.title("Car Price prediction")

    year = st.number_input("enter the mfg year")

    km_driven = st.number_input("enter km driven ")

    # dropdown

    fuel = st.selectbox("Select fuel type", ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])

    seller_type = st.selectbox("Select seller type", ['Dealer', 'Individual', 'Trustmark Dealer'])

    transmission = st.selectbox("Select transmission type", ['Manual', 'Automatic'])

    owner = st.selectbox("Select ownership", ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'])


    # Encoding using if-elif
    if fuel == 'Petrol':
        fuel_encoded = 0
    elif fuel == 'Diesel':
        fuel_encoded = 1
    elif fuel == 'CNG':
        fuel_encoded = 2
    elif fuel == 'LPG':
        fuel_encoded = 3
    else:
        fuel_encoded = 4  # Electric

    if seller_type == 'Individual':
        seller_encoded = 0
    elif seller_type == 'Dealer':
        seller_encoded = 1
    else:
        seller_encoded = 2  # Trustmark Dealer

    if transmission == 'Manual':
        transmission_encoded = 0
    else:
        transmission_encoded = 1  # Automatic

    if owner == 'First Owner':
        owner_encoded = 0
    elif owner == 'Second Owner':
        owner_encoded = 1
    elif owner == 'Third Owner':
        owner_encoded = 2
    elif owner == 'Fourth & Above Owner':
        owner_encoded = 3
    else:
        owner_encoded = 4  # Test Drive Car

    # When the user clicks "Predict"
    if st.button("Predict"):
        input_data = (year, km_driven, fuel_encoded, seller_encoded, transmission_encoded, owner_encoded)
        price, result = car_price_prediction(input_data)
        st.success(f"Predicted Price: ₹{price:,.2f}")
        st.info(f"Suggestion: {result}")

if __name__ == '__main__':
    main()