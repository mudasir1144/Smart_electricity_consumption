import streamlit as st
import pandas as pd
from predictor import ElectricityPredictor
from recommendation import get_recommendations
from utils import (calculate_monthly_consumption,calculate_monthly_bill,get_efficiency_score,format_currency,format_energy)

# Page Configure
st.set_page_config(
    page_title="Smart Electricity Consumption",
    page_icon="⚡",
    layout="wide"
)

# Title
st.title("⚡ Smart Electricity Consumption Prediction System")

st.caption(
    "AI-powered household energy consumption forecasting and optimization."
)

st.info(
    """
This system predicts your household's daily electricity consumption and
provides personalized recommendations to reduce electricity costs.
"""
)

st.divider()

# Load Predictor
try:
    predictor = ElectricityPredictor()
    st.success("✅ Models Loaded Successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()
st.divider()


# Household Information
st.subheader("🏠 Household Information")

col1, col2 = st.columns(2)

with col1:

    house_type = st.selectbox(
        "House Type",
        ["Apartment", "House", "Villa"]
    )

    family_members = st.number_input(
        "Family Members",
        min_value=1,
        max_value=10,
        value=4
    )

    rooms = st.number_input(
        "Rooms",
        min_value=1,
        max_value=10,
        value=4
    )

    season = st.selectbox(
        "Season",
        ["Summer", "Winter", "Spring", "Autumn"]
    )

    day_type = st.selectbox(
        "Day Type",
        ["Weekday", "Weekend", "Holiday"]
    )

with col2:

    ac_hours = st.slider(
        "AC Usage (Hours)",
        0.0, 24.0, 6.0
    )

    fan_hours = st.slider(
        "Fan Usage (Hours)",
        0.0, 24.0, 8.0
    )

    washing_machine = st.slider(
        "Washing Machine Usage (Hours)",
        0.0, 3.0, 1.0
    )

    water_motor = st.slider(
        "Water Motor Usage (Hours)",
        0.0, 3.0, 1.0
    )

    lighting = st.slider(
        "Lighting Hours",
        0.0, 24.0, 8.0
    )

st.divider()


# Environment Information
st.subheader("🌤 Environment Information")

col3, col4 = st.columns(2)

with col3:

    temperature = st.slider(
        "Outdoor Temperature",
        0, 50, 30
    )

    refrigerator = st.selectbox(
        "Refrigerator Available",
        [1, 0],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

with col4:

    work_from_home = st.selectbox(
        "Work From Home",
        ["Yes", "No"]
    )

    solar_panels = st.selectbox(
        "Solar Panels",
        ["Yes", "No"]
    )


# Prediction Button

if st.button("⚡ Predict Electricity Consumption", use_container_width=True):

    input_data = pd.DataFrame([{

        "House_Type": house_type,
        "Family_Members": family_members,
        "Rooms": rooms,
        "AC_Hours": ac_hours,
        "Fan_Hours": fan_hours,
        "Refrigerator": refrigerator,
        "Washing_Machine_Hours": washing_machine,
        "Water_Motor_Hours": water_motor,
        "Lighting_Hours": lighting,
        "Outdoor_Temperature": temperature,
        "Season": season,
        "Day_Type": day_type,
        "Work_From_Home": work_from_home,
        "Solar_Panels": solar_panels

    }])

    daily_consumption = predictor.predict(input_data)
    monthly_consumption = calculate_monthly_consumption(
        daily_consumption
    )

    monthly_bill = calculate_monthly_bill(
        monthly_consumption
    )

    efficiency = get_efficiency_score(
        daily_consumption
    )
    st.divider()
    st.success("Prediction Completed Successfully!")

# ==========================
# Prediction Dashboard
# ==========================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "⚡ Daily Usage",
            format_energy(daily_consumption)
    )

    with col2:
        st.metric(
            "📅 Monthly Usage",
            format_energy(monthly_consumption)
    )

    with col3:
        st.metric(
            "💰 Monthly Bill",
            format_currency(monthly_bill)
    )

    with col4:
        st.metric(
            "⭐ Efficiency",
            efficiency
    )
    st.subheader("💡 Personalized Energy Saving Recommendations")

    recommendations, estimated_savings = get_recommendations(
        ac_hours=ac_hours,
        lighting_hours=lighting,
        washing_machine_hours=washing_machine,
        solar_panels=solar_panels,
        work_from_home=work_from_home
    )

    for recommendation in recommendations:
        st.success(recommendation)
    st.info(
        f"💰 Estimated Monthly Savings: Rs. {estimated_savings:,.0f}"
    )
    st.success("Prediction Completed Successfully!")