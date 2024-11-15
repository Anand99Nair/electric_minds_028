import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load Data
@st.cache_data
def load_data():
    merged_data = pd.read_csv('merged_data.csv')
    merged_data['DATE_TIME'] = pd.to_datetime(merged_data['DATE_TIME'])
    return merged_data

data = load_data()

# Sidebar Filters
st.sidebar.title("Filter Options")
source_keys = st.sidebar.multiselect(
    "Select Source Keys", 
    options=data['SOURCE_KEY'].unique(), 
    default=data['SOURCE_KEY'].unique()
)

date_range = st.sidebar.date_input(
    "Select Date Range", 
    [data['DATE_TIME'].min(), data['DATE_TIME'].max()]
)

# Filter Data
filtered_data = data[
    (data['SOURCE_KEY'].isin(source_keys)) & 
    (data['DATE_TIME'].dt.date >= pd.to_datetime(date_range[0]).date()) & 
    (data['DATE_TIME'].dt.date <= pd.to_datetime(date_range[1]).date())
]

# Main Dashboard
st.title("Solar Power Analysis Dashboard")

# Section 1: Correlation Heatmap
st.header("Correlation Heatmap")
correlation_matrix = filtered_data[['DC_POWER', 'AC_POWER', 'DAILY_YIELD', 'TOTAL_YIELD', 
                                    'AMBIENT_TEMPERATURE', 'MODULE_TEMPERATURE', 'IRRADIATION']].corr()

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
st.pyplot(fig)

# Section 2: Average AC and DC Power by Source Key
st.header("Average AC and DC Power by Source Key")

col1, col2 = st.columns(2)
with col1:
    avg_ac_power = filtered_data.groupby('SOURCE_KEY')['AC_POWER'].mean().reset_index()
    fig = px.bar(avg_ac_power, x='SOURCE_KEY', y='AC_POWER', title="Average AC Power by Source Key")
    st.plotly_chart(fig)

with col2:
    avg_dc_power = filtered_data.groupby('SOURCE_KEY')['DC_POWER'].mean().reset_index()
    fig = px.bar(avg_dc_power, x='SOURCE_KEY', y='DC_POWER', title="Average DC Power by Source Key")
    st.plotly_chart(fig)

# Section 3: Yield Analysis by Source Key
st.header("Yield Analysis by Source Key")
yield_data = filtered_data.groupby('SOURCE_KEY').agg({'DAILY_YIELD': 'mean', 'TOTAL_YIELD': 'mean'}).reset_index()

fig = px.bar(yield_data, x='SOURCE_KEY', y='DAILY_YIELD', title="Average Daily Yield by Source Key")
st.plotly_chart(fig)

# Section 4: Time Series Analysis
st.header("Time Series of DC Power")
fig = px.line(filtered_data, x='DATE_TIME', y='DC_POWER', title="DC Power Over Time")
st.plotly_chart(fig)

# Section 5: Yield vs Temperature
st.header("Daily Yield vs Ambient Temperature")
daily_avg = filtered_data.groupby(filtered_data['DATE_TIME'].dt.date).agg({
    'DAILY_YIELD': 'mean',
    'AMBIENT_TEMPERATURE': 'mean'
}).reset_index()

fig = px.scatter(daily_avg, x='AMBIENT_TEMPERATURE', y='DAILY_YIELD', title="Daily Yield vs Ambient Temperature")
st.plotly_chart(fig)

# Section 6: Temperature Ranges and Yield
st.header("Yield by Temperature Ranges")
bins = [0, 15, 20, 25, 30, 35, 40]
labels = ['<15°C', '15-20°C', '20-25°C', '25-30°C', '30-35°C', '>35°C']
filtered_data['TEMP_RANGE'] = pd.cut(filtered_data['AMBIENT_TEMPERATURE'], bins=bins, labels=labels)

fig = px.box(filtered_data, x='TEMP_RANGE', y='DAILY_YIELD', title="Daily Yield by Temperature Range")
st.plotly_chart(fig)

# Section 7: Irradiation vs Power Output
st.header("Irradiation vs Power Output")
fig = px.scatter(filtered_data, x='IRRADIATION', y='AC_POWER', color='SOURCE_KEY', title="Irradiation vs AC Power")
st.plotly_chart(fig)

fig = px.scatter(filtered_data, x='IRRADIATION', y='DC_POWER', color='SOURCE_KEY', title="Irradiation vs DC Power")
st.plotly_chart(fig)

# Section 8: Total Yield Over Time
st.header("Total Yield Over Time")
daily_total_yield = filtered_data.groupby(filtered_data['DATE_TIME'].dt.date)['TOTAL_YIELD'].sum()

fig = px.line(x=daily_total_yield.index, y=daily_total_yield.values, 
              labels={'x': 'Date', 'y': 'Total Yield (Wh)'}, 
              title="Daily Total Yield Over Time")
st.plotly_chart(fig)

