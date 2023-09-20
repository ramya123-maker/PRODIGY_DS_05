# -*- coding: utf-8 -*-
"""Task 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lyShMM33tPtb-F0Otm4IIbdyfDhRNcqq
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap
sns.set_style("darkgrid")

df = pd.read_csv("https://raw.githubusercontent.com/katreparitosh/Multi-Dimentional-Data-Analytics-of-Road-Accidents-in-India/master/Databases/roadAccStats13-16.csv")

df

df.columns

selected_columns = ['SI. No', 'States/UTs',
       'State/UT-Wise Total Number of Road Accidents during - 2013',
       'State/UT-Wise Total Number of Road Accidents during - 2014',
       'State/UT-Wise Total Number of Road Accidents during - 2015',
       'State/UT-Wise Total Number of Road Accidents during - 2016',
       'Share of States/UTs in Total Number of Road Accidents - 2013',
       'Share of States/UTs in Total Number of Road Accidents - 2014',
       'Share of States/UTs in Total Number of Road Accidents - 2015',
       'Share of States/UTs in Total Number of Road Accidents - 2016',
       'Total Number of Accidents Per Lakh Population - 2013',
       'Total Number of Accidents Per Lakh Population - 2014',
       'Total Number of Accidents Per Lakh Population - 2015',
       'Total Number of Accidents Per Lakh Population - 2016',
       'Total Number of Road Accidents per 10,000 Vehicles - 2013',
       'Total Number of Road Accidents per 10,000 Vehicles - 2014',
       'Total Number of Road Accidents per 10,000 Vehicles - 2015',
       'Total Number of Road Accidents per 10,000 Km of Roads - 2013',
       'Total Number of Road Accidents per 10,000 Km of Roads - 2014',
       'Total Number of Road Accidents per 10,000 Km of Roads - 2015'''],


len(selected_columns)

len(df.columns)

selected_columns = ['SI. No.', 'States/UTs',
       'State/UT-Wise Total Number of Road Accidents during - 2013',
       'State/UT-Wise Total Number of Road Accidents during - 2014',
       'State/UT-Wise Total Number of Road Accidents during - 2015',
       'State/UT-Wise Total Number of Road Accidents during - 2016',
       'Share of States/UTs in Total Number of Road Accidents - 2013',
       'Share of States/UTs in Total Number of Road Accidents - 2014',
       'Share of States/UTs in Total Number of Road Accidents - 2015',
       'Share of States/UTs in Total Number of Road Accidents - 2016',
       'Total Number of Accidents Per Lakh Population - 2013',
       'Total Number of Accidents Per Lakh Population - 2014',
       'Total Number of Accidents Per Lakh Population - 2015',
       'Total Number of Accidents Per Lakh Population - 2016',
       'Total Number of Road Accidents per 10,000 Vehicles - 2013',
       'Total Number of Road Accidents per 10,000 Vehicles - 2014',
       'Total Number of Road Accidents per 10,000 Vehicles - 2015',
       'Total Number of Road Accidents per 10,000 Km of Roads - 2013',
       'Total Number of Road Accidents per 10,000 Km of Roads - 2014',
       'Total Number of Road Accidents per 10,000 Km of Roads - 2015']
weather_df = df[selected_columns].copy()

weather_df.shape

weather_df.info()

missing_percentage = weather_df.isna().sum().sort_values(ascending=False) / len(weather_df)

# Check if there are any missing values before plotting
if missing_percentage[missing_percentage != 0].empty:
    print("No missing values in the DataFrame.")
else:
    missing_percentage[missing_percentage != 0].plot(kind="barh")

weather_df.describe()

weather_df.to_csv('https://raw.githubusercontent.com/katreparitosh/Multi-Dimentional-Data-Analytics-of-Road-Accidents-in-India/master/Databases/roadAccStats13-16.csv', index = False)

weather_df = pd.read_csv("https://raw.githubusercontent.com/katreparitosh/Multi-Dimentional-Data-Analytics-of-Road-Accidents-in-India/master/Databases/roadAccStats13-16.csv")

weather_df['Total Number of Accidents Per Lakh Population - 2016'].count()

weather_df.sample(10)

location_df = weather_df.sample(int(0.1 * len(weather_df)))

print(location_df.columns)

sns.scatterplot(x=location_df['Total Number of Road Accidents per 10,000 Vehicles - 2015'], y=location_df['Total Number of Road Accidents per 10,000 Km of Roads - 2015'], size=0.002)

plt.hist(weather_df['State/UT-Wise Total Number of Road Accidents during - 2016'], bins=np.arange(-20, 80, 10))
plt.xticks(np.arange(-20, 80, 10))
plt.xlabel('State/UT-Wise Total Number of Road Accidents during - 2015', fontsize=12)
plt.ylabel('Share of States/UTs in Total Number of Road Accidents - 2016', fontsize=12)

row, column = df.shape

# CALCULATE Usefullness of columns
round(((row - df.isnull().sum())/ row) * 100,2)

df.duplicated()

df['States/UTs'].value_counts()

mean13 = np.mean(df['State/UT-Wise Total Number of Road Accidents during - 2013'])
print("Mean of accidents happened in all states in year 2013: {}".format(mean13))

mean14 = np.mean(df['State/UT-Wise Total Number of Road Accidents during - 2014'])
print("Mean of accidents happened in all states in year 2014 : {}".format(mean14))

mean15 = np.mean(df['State/UT-Wise Total Number of Road Accidents during - 2015'])
print("Mean of accidents happened in all states in year 2015 : {}".format(mean15))

mean16 = np.mean(df['State/UT-Wise Total Number of Road Accidents during - 2016'])
print("Mean of accidents happened in all states in 2016 {}".format(mean16))

import matplotlib.pyplot as plt

# Data
labels = 'State/UT-Wise Total Number of Road Accidents during - 2013', 'State/UT-Wise Total Number of Road Accidents during - 2014', 'State/UT-Wise Total Number of Road Accidents during - 2015', 'State/UT-Wise Total Number of Road Accidents during - 2016'
sizes = [mean13, mean14, mean15, mean16]
colors = ['gold', 'green', 'blue', 'orange']
explode = (0.01, 0.01, 0.01, 0.01)

# Create a pie chart with custom properties
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, explode=explode,
       shadow=True, autopct='%.4f%%', startangle=140, wedgeprops={'edgecolor': 'black', 'linewidth': 2}, radius=0.75)

# Create a circle in the center to make it a donut chart
centre_circle = plt.Circle((0, 0), 0.5, color='black', fc='white', linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')
plt.title('Custom Pie Chart')
plt.show()

# Data
y = df['State/UT-Wise Total Number of Road Accidents during - 2013']
yd = df['States/UTs']
p = df['States/UTs'].nunique()
d = np.arange(p)  # Use np.arange to create an array of indices

# Create a bar graph with custom formatting
plt.figure(figsize=(12, 8))  # Adjust the figure size
plt.barh(d, y, color='skyblue')  # Use barh for horizontal bars
plt.yticks(d, yd)  # Set y-tick labels
plt.xlabel('Number of Accidents')  # Label for the x-axis
plt.title('Total Number of Accidents in Each State (2013)')  # Title of the graph

# Add data values on the bars
for i, value in enumerate(y):
    plt.text(value, i, f' {value}', va='center', fontsize=12, color='black')

# Add grid lines
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.show()

min13 = np.min(df['Total Number of Accidents Per Lakh Population - 2013'])
max13 = np.max(df['Total Number of Accidents Per Lakh Population - 2013'])
min14 = np.min(df['Total Number of Accidents Per Lakh Population - 2014'])
max14 = np.max(df['Total Number of Accidents Per Lakh Population - 2014'])
min15 = np.min(df['Total Number of Accidents Per Lakh Population - 2015'])
max15 = np.max(df['Total Number of Accidents Per Lakh Population - 2015'])
min16 = np.min(df['Total Number of Accidents Per Lakh Population - 2016'])
max16 = np.max(df['Total Number of Accidents Per Lakh Population - 2016'])

# Data
n = 4
minx = (min13, min14, min15, min16)
maxx = (max13, max14, max15, max16)
years = ('2013', '2014', '2015', '2016')

# Set the figure size
plt.figure(figsize=(10, 6))

# Create bar positions for each year
index = np.arange(n)
bar_width = 0.4

# Create bars for the minimum values
plt.bar(index, minx, bar_width, label='Min', color='b', alpha=0.7)

# Create bars for the maximum values
plt.bar(index, maxx, bar_width, label='Max', color='pink', alpha=0.7, bottom=minx)

# Add labels and title
plt.xlabel("Year")
plt.ylabel("Number of Accidents")
plt.title("Min and Max Number of Accidents per Year")

# Set the x-axis ticks and labels
plt.xticks(index + bar_width / 2, years)

# Add legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()

df6 = pd.read_csv('https://raw.githubusercontent.com/katreparitosh/Multi-Dimentional-Data-Analytics-of-Road-Accidents-in-India/master/Databases/typeOfVehicle.csv')
df6.head()

row, column = df6.shape
round(((row - df6.isnull().sum())/row)*100)

df6.dropna(axis = 0, how = 'any', inplace = True)

import matplotlib.pyplot as plt
import numpy as np

# Data
UT = np.arange(1, 38)
vehicle_types = ['Two-Wheelers', 'Auto-Rickshaws', 'Cars, Jeeps, Taxis', 'Buses',
                 'Trucks, Tempos, MAVs, Tractors', 'Other Motor Vehicles', 'Other Vehicles/Objects']

# Define colors for each vehicle type
colors = ['r', 'black', 'g', 'b', 'yellow', 'brown', 'purple']

# Create subplots for better readability
fig, ax = plt.subplots(figsize=(20, 10))
plt.rcParams.update({'font.size': 18})

bar_width = 0.1
bar_positions = UT - 0.3

# Loop through each vehicle type and plot the bars
for i, vehicle_type in enumerate(vehicle_types):
    bar_data = df6[f'{vehicle_type} - Number of Road Accidents - Total - 2014 per 1L people']
    ax.bar(bar_positions + i * bar_width, bar_data, width=bar_width, color=colors[i], label=vehicle_type)

# Customize the x-axis labels and rotate them vertically for better readability
ax.set_xticks(UT)
ax.set_xticklabels(df6['States/UTs'], rotation='vertical')

# Add legend
ax.legend(loc="best")

# Add title and labels
ax.set_title("Number of Total Accidents for Each Vehicle Type per 1L People in Each State")
ax.set_xlabel("States/UTs")
ax.set_ylabel("Accidents per 1L People")

# Show the plot
plt.tight_layout()
plt.show()

plt.figure(figsize=(20,10))
plt.rcParams.update({'font.size':18})

plt.bar(UT-0.6,df6['Two-Wheelers - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='r',align='center',label='Two-Wheelers')
plt.bar(UT-0.4,df6['Auto-Rickshaws - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='black',align='center',label='Auto-Rickshaws')
plt.bar(UT-0.2,df6['Cars, Jeeps,Taxis - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='g',align='center',label='Cars,Jeeps,Taxis')
plt.bar(UT,df6['Buses - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='b',align='center',label='Buses')
plt.bar(UT+0.2,df6['Trucks, Tempos,MAVs,Tractors - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Trucks, Tempos,MAVs,Tractors')
plt.bar(UT+0.4,df6['Other Motor Vehicles - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='brown',align='center',label='Other Motor Vehicles')
plt.bar(UT+0.6,df6['Other Vehicles/Objects - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='purple',align='center',label='Other Vehicles/Objects')

plt.xticks(UT,df6['States/UTs'],rotation='vertical')
plt.legend(loc='upper left', bbox_to_anchor=(0.2,1))
plt.title("Number of Fatal Accidents for each vehicle type per 1L people of that state")
plt.show()

plt.figure(figsize=(20,10))
plt.rcParams.update({'font.size':18})

plt.bar(UT-0.6,df6['Two-Wheelers - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='r',align='center',label='Two-Wheelers')
plt.bar(UT-0.4,df6['Auto-Rickshaws - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='black',align='center',label='Auto-Rickshaws')
plt.bar(UT-0.2,df6['Cars, Jeeps,Taxis - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='g',align='center',label='Cars,Jeeps,Taxis')
plt.bar(UT,df6['Buses - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='b',align='center',label='Buses')
plt.bar(UT+0.2,df6['Trucks, Tempos,MAVs,Tractors - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Trucks, Tempos,MAVs,Tractors')
plt.bar(UT+0.4,df6['Other Motor Vehicles - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='brown',align='center',label='Other Motor Vehicles')
plt.bar(UT+0.6,df6['Other Vehicles/Objects - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='purple',align='center',label='Other Vehicles/Objects')

plt.xticks(UT,df6['States/UTs'],rotation='vertical')
plt.legend(loc='upper left', bbox_to_anchor=(0.25,1))
plt.title("Number of Persons Killed for each vehicle type per 1L people of that state")
plt.show()

plt.figure(figsize=(20,10))
plt.rcParams.update({'font.size':18})

plt.bar(UT-0.6,df6['Two-Wheelers - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='r',align='center',label='Two-Wheelers')
plt.bar(UT-0.4,df6['Auto-Rickshaws - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='black',align='center',label='Auto-Rickshaws')
plt.bar(UT-0.2,df6['Cars, Jeeps,Taxis - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='g',align='center',label='Cars,Jeeps,Taxis')
plt.bar(UT,df6['Buses - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='b',align='center',label='Buses')
plt.bar(UT+0.2,df6['Trucks, Tempos,MAVs,Tractors - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Trucks, Tempos,MAVs,Tractors')
plt.bar(UT+0.4,df6['Other Motor Vehicles - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='brown',align='center',label='Other Motor Vehicles')
plt.bar(UT+0.6,df6['Other Vehicles/Objects - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='purple',align='center',label='Other Vehicles/Objects')

plt.xticks(UT,df6['States/UTs'],rotation='vertical')
plt.legend(loc='upper left', bbox_to_anchor=(0.25,1))
plt.title("Number of Persons Killed for each vehicle type per 1L people of that state")
plt.show()

plt.figure(figsize=(20,10))
plt.rcParams.update({'font.size':18})

plt.bar(UT-0.6,df6['Two-Wheelers - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='r',align='center',label='Two-Wheelers')
plt.bar(UT-0.4,df6['Auto-Rickshaws - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='black',align='center',label='Auto-Rickshaws')
plt.bar(UT-0.2,df6['Cars, Jeeps,Taxis - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='g',align='center',label='Cars,Jeeps,Taxis')
plt.bar(UT,df6['Buses - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='b',align='center',label='Buses')
plt.bar(UT+0.2,df6['Trucks, Tempos,MAVs,Tractors - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Trucks, Tempos,MAVs,Tractors')
plt.bar(UT+0.4,df6['Other Motor Vehicles - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='brown',align='center',label='Other Motor Vehicles')
plt.bar(UT+0.6,df6['Other Vehicles/Objects - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='purple',align='center',label='Other Vehicles/Objects')

plt.xticks(UT,df6['States/UTs'],rotation='vertical')
plt.legend(loc='upper left', bbox_to_anchor=(0.9,1))
plt.title("Number of Persons Injured for each vehicle type per 1L people of that state")
plt.show()

plt.figure(figsize=(20,10))
plt.rcParams.update({'font.size':18})
UT=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37])

plt.bar(UT-0.4,df6['Two-Wheelers - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='r',align='center',label='Injured')
plt.bar(UT-0.2,df6['Two-Wheelers - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='g',align='center',label='Killed')
plt.bar(UT,df6['Two-Wheelers - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='b',align='center',label='Total Accidents')
plt.bar(UT+0.2,df6['Two-Wheelers - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Fatal Accidents')

plt.xticks(UT,df6['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Persons Injured, Killed; Road Accidents Total and fatal for 2 wheelers per 1L people of that state")
plt.show()

plt.figure(figsize=(20,10))
plt.rcParams.update({'font.size':18})

plt.bar(UT-0.4,df6['Cars, Jeeps,Taxis - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='r',align='center',label='Injured')
plt.bar(UT-0.2,df6['Cars, Jeeps,Taxis - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='g',align='center',label='Killed')
plt.bar(UT,df6['Cars, Jeeps,Taxis - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='b',align='center',label='Total Accidents')
plt.bar(UT+0.2,df6['Cars, Jeeps,Taxis - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Fatal Accidents')

plt.xticks(UT,df6['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Persons Injured, Killed; Road Accidents Total and fatal for Cars, Jeeps and Taxis per 1L people of that state")
plt.show()

plt.figure(figsize=(20,10))
plt.rcParams.update({'font.size':18})

plt.bar(UT-0.4,df6['Buses - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='r',align='center',label='Injured')
plt.bar(UT-0.2,df6['Buses - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='g',align='center',label='Killed')
plt.bar(UT,df6['Buses - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='b',align='center',label='Total Accidents')
plt.bar(UT+0.2,df6['Buses - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Fatal Accidents')

plt.xticks(UT,df6['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Persons Injured, Killed; Road Accidents Total and fatal for Buses per 1L people of that state")
plt.show()

plt.figure(figsize=(20,10))
plt.rcParams.update({'font.size':18})

plt.bar(UT-0.4,df6['Trucks, Tempos,MAVs,Tractors - Number of Persons - Injured - 2014 per 1L people'],width=0.2,color='r',align='center',label='Injured')
plt.bar(UT-0.2,df6['Trucks, Tempos,MAVs,Tractors - Number of Persons - Killed - 2014 per 1L people'],width=0.2,color='g',align='center',label='Killed')
plt.bar(UT,df6['Trucks, Tempos,MAVs,Tractors - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='b',align='center',label='Total Accidents')
plt.bar(UT+0.2,df6['Trucks, Tempos,MAVs,Tractors - Number of Road Accidents - Fatal - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Fatal Accidents')

plt.xticks(UT,df6['States/UTs'],rotation='vertical')
plt.legend(loc="best")
plt.title("Number of Persons Injured, Killed; Road Accidents Total and fatal for Trucks and Tractors per 1L people of that state")
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap
sns.set_style("darkgrid")

df1 = pd.read_csv("https://raw.githubusercontent.com/damianoc90/Road-accidents-analysis/master/dataset.csv")

df1

df2 = pd.read_csv('https://raw.githubusercontent.com/IndiraBobburi/accident-severity-prediction/master/sample_test_data_jupyter.csv', sep=',')

df2

print(df2['Light_Conditions'].value_counts())
encoding_light = {"Light_Conditions": {"Daylight": 0, "Darkness - lights lit": 1, "Darkness - no lighting": 1, "Darkness - lighting unknown": 1, "Darkness - lights unlit": 1, "Data missing or out of range": 0}}
df2.replace(encoding_light, inplace=True)
print(df2['Light_Conditions'].value_counts())

print(df2['Day_of_Week'].value_counts())
encoding_day_of_week = {"Day_of_Week": {"Saturday": 1, "Sunday": 1, "Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0}}
df2.replace(encoding_day_of_week, inplace=True)
print(df2['Day_of_Week'].value_counts())

print(df2['Special_Conditions_at_Site'].value_counts())
encoding_Special_Conditions_at_Site = {"Special_Conditions_at_Site": {"None": 0, "Roadworks": 1, "Oil or diesel": 1, "Mud": 1, "Road surface defective": 1, "Auto traffic signal - out": 1, "Road sign or marking defective or obscured": 1, "Auto signal part defective": 1, "Data missing or out of range": 0}}
df2.replace(encoding_Special_Conditions_at_Site, inplace=True)
print(df2['Special_Conditions_at_Site'].value_counts())

encoding_road_surface_cond = {"Road_Surface_Conditions":
                            {"Dry": 1,
                             "Wet or damp": 2,
                             "Frost or ice": 3,
                             "Snow": 4,
                             "Flood over 3cm. deep": 5,
                             "Data missing or out of range": 1 }}
df2.replace(encoding_road_surface_cond, inplace=True)
df2['Road_Surface_Conditions'].value_counts()

encoding_road_type = {"Road_Type":
                            {"Single carriageway": 1,
                             "Dual carriageway": 2,
                             "Roundabout": 3,
                             "One way street": 4,
                             "Slip road": 5,
                             "Unknown": 0,
                             "Data missing or out of range": 1 }}
df2.replace(encoding_road_type, inplace=True)
df2['Road_Type'].value_counts()

encoding_weather = {"Weather_Conditions":
                            {"Fine no high winds": 1,
                             "Raining no high winds": 2,
                             "Raining + high winds": 3,
                             "Fine + high winds": 4,
                             "Snowing no high winds": 5,
                             "Fog or mist": 6,
                             "Snowing + high winds": 7,
                             "Unknown": 1,
                             "Other": 1,
                             "Data missing or out of range": 1 }}
df2.replace(encoding_weather, inplace=True)
df2['Weather_Conditions'].value_counts()

df2['Time'].fillna(0, inplace=True)

def period(row):
    rdf = []
    if(type(row) == float):
        row = str(row)
        rdf = row.split(".")
    else:
        rdf = str(row).split(":"); # day -- 8am-8pm

    hr = rdf[0]
    if int(hr) > 8 and int(hr) < 20:
        return 1;
    else:
        return 2;

df2['Time'] = df2['Time'].apply(period)

df2_train1 = df2[['1st_Road_Class','Carriageway_Hazards','Junction_Control','Day_of_Week','Junction_Detail','Light_Conditions']]

import numpy as np

# Rest of your code
mean20 = np.mean(df2['Day_of_Week'])
print("Mean of Day_of_Week: {}".format(mean20))

import numpy as np

# Rest of your code
mean21 = np.mean(df2['Light_Conditions'])
print("Mean of Light_Conditions: {}".format(mean21))

import numpy as np

# Rest of your code
mean22 = np.mean(df2['Weather_Conditions'])
print("Mean of Weather_Conditions: {}".format(mean22))

labels = 'Day_of_Week','Light_Conditions','Weather_Conditions'
sizes = [mean20, mean21, mean22]
colors = ['gold', 'green', 'blue']
explode = (0.01, 0.01, 0.01)
plt.pie(sizes, labels = labels, colors = colors, explode = explode,
       shadow = True, autopct = '%.4f%%', startangle = 140)
plt.axis('equal')
plt.show()

