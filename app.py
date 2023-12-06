import streamlit as st
import pickle5 as pickle
from sklearn.ensemble import RandomForestRegressor



def Predict(input_list,loaded_model):
    predictions = loaded_model.predict([input_list])
    return predictions
def main():
    with open('trained_model.pkl', 'rb') as model_file:
        loaded_model = pickle.load(model_file)

# Load metadata
    with open('model_metadata.pkl', 'rb') as metadata_file:
        loaded_metadata = pickle.load(metadata_file)
    st.title("Input Form to List Converter")

    # Get numerical inputs from the user
    tool_diameter = st.number_input("Tool Diameter", value=0.0)
    spindle_speed = st.number_input("Spindle Speed", value=0.0)
    step_depth = st.number_input("Step Depth", value=0.0)
    feed_rate = st.number_input("Feed Rate", value=0.0)

    # Get categorical inputs from the user
    material_options = ["Material_AZ31", "Material_AZ61"]
    material = st.selectbox("Material", material_options)

    test_type_options = ["Test type_SG", "Test type_VWA"]
    test_type = st.selectbox("Test Type", test_type_options)

    # Convert inputs to a list
    input_list = [tool_diameter, spindle_speed, step_depth, feed_rate, material, test_type]

    # Display the input list
    st.subheader("Input List:")
    st.write(input_list)

    if st.button("Predict"):
        predictions = Predict(input_list,loaded_model)
        st.subheader("Prediction:")
        st.write(predictions)

if __name__ == "__main__":
    main()
