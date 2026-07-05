import streamlit as st
import pandas as pd
from predictor import ElectricityPredictor

# Page Configuration

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

st.info("""
This system predicts your household's daily electricity consumption and provides
personalized recommendations to help reduce electricity costs.
""")

st.divider()

try:
    predictor = ElectricityPredictor()
    st.success('Model Loaded Successfully')
except Exception as e:
    st.error(f"Error loading model:{e}")

# Household Information

st.subheader("🏠 Household Information")
st.caption("Enter basic information about your home.")

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

# Environment

st.divider()

st.subheader("🌤 Environment Information")
st.caption("Weather and lifestyle factors affecting electricity usage.")

col3, col4 = st.columns(2)

with col3:

    temperature = st.slider(
        "Outdoor Temperature",
        0,
        50,
        30
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

# Predict Button

predict_button = st.button(
    "⚡ Predict Electricity Consumption",
    use_container_width=True
)

# Prediction

if predict_button:

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

    daily_consumption= predictor.predict(input_data)

    monthly_consumption = round(daily_consumption * 30, 2)
    electricity_rate = 65
    monthly_bill = round(monthly_consumption * electricity_rate, 2)
    # Efficiency Score

    if daily_consumption < 15:
        efficiency = "Excellent ⭐⭐⭐⭐⭐"
    elif daily_consumption < 25:
        efficiency = "Good ⭐⭐⭐⭐"
    elif daily_consumption < 35:
        efficiency = "Average ⭐⭐⭐"
    else:
        efficiency = "High Consumption ⭐⭐"
    st.success("Prediction Completed Successfully!")

    # Dashboard    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(
            "⚡ Daily Usage",
            f"{daily_consumption} kWh"
        )
    with col2:
        st.metric(
            "📅 Monthly Usage",
            f"{monthly_consumption} kWh"
        )
    with col3:
        st.metric(
            "💰 Monthly Bill",
            f"Rs. {monthly_bill:,.0f}"
        )
    with col4:
        st.metric(
            "⭐ Efficiency",
            efficiency
        )
    # Recommendation System for model results
    st.divider()

    st.subheader("💡 Energy Saving Recommendations")

    recommendations = []

    estimated_savings = 0

    if ac_hours > 8:
        recommendations.append(
            "❄️ Reduce AC usage by 1–2 hours during hot afternoons."
        )
        estimated_savings += 800

    if lighting > 8:
        recommendations.append(
            "💡 Replace conventional bulbs with LED lighting."
        )
        estimated_savings += 400

    if washing_machine > 1.5:
        recommendations.append(
            "🧺 Operate the washing machine during off-peak hours."
        )
        estimated_savings += 300

    if solar_panels == "No":
        recommendations.append(
            "☀️ Installing solar panels can significantly reduce electricity costs."
        )
        estimated_savings += 2500

    if work_from_home == "Yes":
        recommendations.append(
            "💻 Turn off idle electronics while working."
        )
        estimated_savings += 200

    if recommendations:
        for rec in recommendations:
            st.success(rec)
    else:
        st.success(
            "🎉 Excellent! Your household is already energy efficient."
        )
    st.info(
        f"💰 Estimated Monthly Savings: Rs. {estimated_savings:,.0f}"
    )
st.divider()
