import streamlit as st
import numpy as np
import pickle
import sklearn


# import the model
model = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title('House Rent Predictor')

col1,col2 = st.columns(2)

with col1:

    # bhk
    bhk=st.selectbox('BHK',df['bhk'].unique())

    # locality
    loc=st.selectbox('Locality',df['locality'].unique())

    # latitude
    lat=st.number_input('Latitude')

    # longitude
    long=st.number_input('Longitude')

    # lease_type
    lease=st.selectbox('Lease Type',df['lease_type'].unique())

    # gym
    gym = st.selectbox('Gym',['No','Yes'])

    # lift
    lift = st.selectbox('Lift',['No','Yes'])

    # swimming pool
    pool = st.selectbox('Swimming Pool',['No','Yes'])

    # negotiable
    neg = st.selectbox('Negotiable', ['No', 'Yes'])

    # furnishing
    furnish = st.selectbox('Furnishing', df['furnishing'].unique())


with col2:
    # parking
    park = st.selectbox('Parking',df['parking'].unique())

    # propert size
    prop_size = st.number_input('Property Size')

    # propert age
    prop_age = st.number_input('Property Age')

    # bathroom
    bath = st.number_input('Bathroom')

    # facing
    face = st.selectbox('Facing',df['facing'].unique())

    # cupboard
    cb = st.number_input('CupBoard')

    # floor
    floor = st.number_input('Floor')

    # balconies
    bal = st.number_input('No. of Balconies')

    # Water Supply
    water = st.selectbox('Water Supply',df['water_supply'].unique())

    # Building Type
    building = st.selectbox('Building Type',df['building_type'].unique())


if st.button('Predict Rent'):
    if gym == 'Yes':
        gym = 1
    else:
        gym = 0

    if lift == 'Yes':
        lift = 1
    else:
        lift = 0

    if pool == 'Yes':
        pool = 1
    else:
        pool = 0

    if neg == 'Yes':
        neg = 1
    else:
        neg = 0

    query = np.array([bhk, loc, lat, long, lease, gym, lift, pool,neg, furnish, park, prop_size,prop_age,bath,face,cb,floor,water,building,bal])
    query = query.reshape(1, 20)
    st.title("The predicted rent of this type of house is Rs." + str(int(model.predict(query)[0])))
