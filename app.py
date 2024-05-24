import pickle
import streamlit as st
import numpy as np

model = pickle.load(open('lasso_model.pkl', 'rb'))

def map_categorical_to_num(value, categories):
    """
    Maps categorical input to numerical values.
    """
    return categories.index(value)

def main():
    st.title('Energy Consumption Prediction System')

    # Input variables
    Temperature = st.text_input('Temperature')
    Humidity = st.text_input('Humidity in Percentage')
    SquareFootage = st.text_input('Square Footage')
    Occupancy = st.text_input('Occupancy')
    HVACUsage = st.selectbox('HVAC Usage', ['Off', 'On'])
    LightingUsage = st.selectbox('Lighting Usage', ['Off', 'On'])
    DayOfWeek = st.selectbox('Day Of Week', ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
    Holiday = st.selectbox('Holiday', ['No', 'Yes'])

    # Map categorical variables to numerical values
    HVACUsage_mapped = map_categorical_to_num(HVACUsage, ['Off', 'On'])
    LightingUsage_mapped = map_categorical_to_num(LightingUsage, ['Off', 'On'])
    DayOfWeek_mapped = map_categorical_to_num(DayOfWeek, ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
    Holiday_mapped = map_categorical_to_num(Holiday, ['No', 'Yes'])

    # Combine input features
    features = [Temperature, Humidity,SquareFootage,Occupancy,HVACUsage_mapped, LightingUsage_mapped, DayOfWeek_mapped, Holiday_mapped]

    # Prediction Code
    if st.button('Predict'):
        make_predictions = model.predict([features)
        output = round(make_predictions[0], 2)
        st.success('Energy Consumption will be {} kW'.format(output))

if __name__ == '__main__':
    main()

