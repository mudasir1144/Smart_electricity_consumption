import numpy as np
import pandas as pd
import random

#Using seed to make data reproducible
random.seed(42)
np.random.seed(42)

#Making 500 records of data
new_record = 500

#defining categries
house_types=['Apartment','House','Villa']
seasons = ['Summer','Winter','Spring','Autumn']
day_types=['Weekday','Weekend','Holiday']

#Defining selection probability
house_prob = [0.45,0.40,0.15]
season_prob=[0.25,0.25,0.25,0.25]
day_types_prob=[0.70,0.20,0.10]

data=[]

#Using loop to create random data for each record
for _ in range(new_record):
    house_type = np.random.choice(house_types, p=house_prob)
    
    family_members = np.random.choice(
        [1,2,3,4,5,6,7,8],
        p=[0.05,0.15,0.20,0.20,0.20,0.10,0.05,0.05])


    if house_type == 'Apartment':
        rooms = random.randint(2,4)
    elif house_type =='House':
        rooms = random.randint(3,6)
    else:
        rooms = random.randint(5,8)
    
    season = np.random.choice(seasons,p=season_prob)

    if season == 'Summer':
        temperature = round(random.uniform(32,45),1)
    elif season == 'Winter':
        temperature = round(random.uniform(5,18),1)
    elif season =='Spring':
        temperature = round(random.uniform(22,32),1)
    else:
        temperature = round(random.uniform(18,25),1)

    day_type = np.random.choice(day_types,p=day_types_prob)

    work_from_home = np.random.choice(
        ['Yes','No'],
        p=[0.30,0.70]
    )

    solar_panels = np.random.choice(
        ['Yes','No'],
        p=[0.20,0.80]
    )

    refrigerator = np.random.choice(
        [0,1],
        p=[0.05,0.95]
    )

    if season =='Summer':
        ac_hours = round(random.uniform(6,18),1)
    elif season =='Winter':
        ac_hours = round(random.uniform(0,3),1)
    elif season =='Spring':
        ac_hours = round(random.uniform(2,8),1)
    else:
        ac_hours = round(random.uniform(1,6),1)

    fan_hours =round(min(24,max(2,temperature/2+random.uniform(-2,2))),1)

    washing_mach_hours = round(random.uniform(0.2, 1.2) * (family_members / 3),1)
    washing_mach_hours=min(washing_mach_hours,3)

    if house_type=='Apartment':
        water_motor_hours = round(random.uniform(0.2,1.0),1)
    elif house_type == 'House':
        water_motor_hours = round(random.uniform(0.5,2.0),1)
    else: 
        water_motor_hours = round(random.uniform(1.0,3.0),1)

    lighting_hours = round(random.uniform(4,8)+rooms*0.8+family_members*0.3,1)


    base_load=3

    ac_consumption = ac_hours *1.5
    fan_consumption = fan_hours * 0.08
    refrigerator_consumption = refrigerator*1.2
    washing_mach_consumption = washing_mach_hours*0.5
    motor_consumption = water_motor_hours*0.75
    lighting_consumption = lighting_hours*0.12
    family_consumption = family_members*0.25
    if work_from_home =='Yes':
        wfh_consumption = 1.5
    else:
        wfh_consumption = 0
    temprature_effect = max(0,(temperature-25)*0.15)
    if solar_panels == 'Yes':
        solar_offset=2
    else:
        solar_offset=0
    noise = random.uniform(-1,1)

    daily_consumption = (
        base_load
        + ac_consumption
        + fan_consumption
        + refrigerator_consumption
        + washing_mach_consumption
        + motor_consumption
        + lighting_consumption
        + family_consumption
        + wfh_consumption
        + temprature_effect
        - solar_offset
        + noise
    )
    
    daily_consumption = round(
    max(daily_consumption, 1),2)

    record = {
        "House_Type": house_type,
        "Family_Members": family_members,
        "Rooms": rooms,
        "AC_Hours": ac_hours,
        "Fan_Hours": fan_hours,
        "Refrigerator": refrigerator,
        "Washing_Machine_Hours": washing_mach_hours,
        "Water_Motor_Hours": water_motor_hours,
        "Lighting_Hours": lighting_hours,
        "Outdoor_Temperature": temperature,
        "Season": season,
        "Day_Type": day_type,
        "Work_From_Home": work_from_home,
        "Solar_Panels": solar_panels,
        "Daily_Electricity_Consumption": daily_consumption
    }

    data.append(record)
data = pd.DataFrame(data)
data.to_csv(
    "C:\\Users\\HP\\OneDrive\\Desktop\\Intern project\\Smart-Electricity-Consumption\\dataset\\electricity_dataset.csv",
    index=False
)


print("\nDataset Generated Successfully!")
print("-" * 50)

print(f"Total Records : {len(data)}")
print(f"Total Features: {len(data.columns)}")

print("\nFirst Five Rows")
print(data.head())

print("\nStatistical Summary")
print(data.describe())

