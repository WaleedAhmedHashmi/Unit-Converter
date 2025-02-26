import streamlit as st

def convert_units(value, from_unit, to_unit, category):
    conversions = {
        "Length": {
            "meters": 1, "kilometers": 0.001, "miles": 0.000621371, "centimeters": 100
        },
        "Area": {
            "square meters": 1, "square kilometers": 0.000001, "square miles": 0.000000386102, 
            "square inch": 1550
        },
        "Temperature": {
            "Celsius": lambda x: x, 
            "Fahrenheit": lambda x: (x * 9/5) + 32,
            "Kelvin": lambda x: x + 273.15
        }
    }
    
    if category == "Temperature":
        return conversions[category][to_unit](value)
    else:
        return value * (conversions[category][to_unit] / conversions[category][from_unit])

st.title("Unit Converter")

category = st.selectbox("Select Category", ["Length", "Area", "Temperature"])

units = {
    "Length": ["meters", "kilometers", "miles", "centimeters"],
    "Area": ["square meters", "square kilometers", "square miles", "square inch"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

from_unit = st.selectbox("From Unit", units[category])
to_unit = st.selectbox("To Unit", units[category])
value = st.number_input("Enter Value", value=0.0, format="%.2f")

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
