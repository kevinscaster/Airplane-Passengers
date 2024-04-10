import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/Users/kevin.caster/Downloads/AirPassengers.csv'
df = pd.read_csv(file_path)
# Set page layout to wide
st.set_page_config(layout="wide")

# Convert 'Month' column to datetime format
df['Month'] = pd.to_datetime(df['Month'])

# Title
st.title('Airline Passenger Dashboard')

# Display the dataset and total number of passengers in a two-column layout
col1, col2 = st.columns([2, 1])

# Display the dataset in the left column
with col1:
    st.subheader('Dataset')
    st.write(df)

# Display the total number of passengers in the right column
with col2:
    st.subheader('Total Number of Passengers')
    total_passengers = df['#Passengers'].sum()
    st.write(f'Total Passengers: {total_passengers}')

# Add separator line 
st.markdown('<hr style="border: 2px solid blue;">', unsafe_allow_html=True)

# Interactive control for moving average window size
window_size = st.slider('Moving Average Window Size', min_value=1, max_value=24, value=12, step=1)

# Calculate the moving average for the number of passengers based on the selected window size
df['Moving Average'] = df['#Passengers'].rolling(window=window_size).mean()

# Monthly passenger trends (line chart)
st.subheader('Monthly Passenger Trends')
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df['Month'], df['#Passengers'], label='Passengers')
ax.plot(df['Month'], df['Moving Average'], label=f'Moving Average (Window Size: {window_size})', linestyle='--')
ax.set_xlabel('Month')
ax.set_ylabel('Passengers')
ax.set_title('Monthly Passenger Trends')
ax.legend()
st.pyplot(fig)

# Close the plot to prevent overlapping in Streamlit
plt.close()
