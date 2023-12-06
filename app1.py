import streamlit as st
import pandas as pd
import pickle

def load_model():
    with open('model3.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    return model

def main():
    st.title("Formability Prediction App")

    # Load the trained model
    model = load_model()

    # Get user inputs
    tool_diameter = st.number_input("Tool Diameter", value=0)
    spindle_speed = st.number_input("Spindle Speed", value=0)
    step_depth = st.number_input("Step Depth", value=0.0)
    feed_rate = st.number_input("Feed Rate", value=0)
    AZ31 = st.number_input("Material-AZ31", value=0)
    AZ61 = st.number_input("Material-AZ61", value=0)
    SG = st.number_input("Test Type-SG", value=0)
    VWA = st.number_input("Test Type-VWA", value=0)
    #material = st.selectbox("Material", ["AZ31", "AZ61"])
    #test_type = st.selectbox("Test Type", ["SG", "VWA"])

    # Create a DataFrame with user inputs
    input_data = pd.DataFrame({
        'Tool diameter': [tool_diameter],
        'Spindle speed': [spindle_speed],
        'Step depth': [step_depth],
        'Feed rate': [feed_rate],
        'Material_AZ31': [AZ31],
        'Material_AZ61': [AZ61],
        'Test type_SG': [SG],
        'Test type_VWA': [VWA]
    })

    # One-hot encode categorical variables using pd.get_dummies
    #input_data_encoded = pd.get_dummies(input_data, columns=['Material', 'Test type'])
    #print(input_data.head())
    #print(input_data_encoded.head())

    # Display the input data
    st.subheader("Input Data:")
    st.write(input_data)

    # Make a prediction
    if st.button("Predict"):
        prediction = model.predict(input_data)
        st.subheader("Prediction:")
        st.write(f"The predicted formability is: {prediction[0]}")

if __name__ == "__main__":
    main()
