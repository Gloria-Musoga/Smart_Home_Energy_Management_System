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
    Occupancy = st.text_input('Occupancy')
    HVACUsage = st.selectbox('HVAC Usage', ['Off', 'On'])
    LightingUsage = st.selectbox('Lighting Usage', ['Off', 'On'])

    # Map categorical variables to numerical values
    HVACUsage_mapped = map_categorical_to_num(HVACUsage, ['Off', 'On'])
    LightingUsage_mapped = map_categorical_to_num(LightingUsage, ['Off', 'On'])
    

    # Combine input features
    features = [float(Temperature),int(Occupancy),HVACUsage_mapped, LightingUsage_mapped]

    # Prediction Code
    if st.button('Predict'):
        make_predictions = model.predict([features])
        output = round(make_predictions[0], 2)
        st.success('Energy Consumption will be {} kW'.format(output))

if __name__ == '__main__':
    main()

