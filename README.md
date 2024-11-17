# Solar Power Analysis Dashboard

## Overview

The **Solar Power Analysis Dashboard** is an interactive web application built with **Streamlit** for the visualization and analysis of solar power generation data. This project aims to provide a comprehensive understanding of the key performance metrics related to solar power systems, such as DC power, AC power, daily yield, and total yield. The dashboard leverages **Plotly**, **Seaborn**, and **Matplotlib** for interactive and static visualizations, while **Pandas** is used for efficient data manipulation.

This tool allows users to explore solar energy data in multiple ways, including time series analysis, correlations, and yield comparisons based on various parameters like temperature, irradiation, and source key. Users can apply filters to customize the displayed data by selecting specific source keys and date ranges.

---

## Features

### 1. **Correlation Heatmap**
   - Visualizes the correlation between key solar power metrics such as DC power, AC power, daily yield, total yield, ambient temperature, module temperature, and irradiation using a heatmap.

### 2. **Average AC and DC Power by Source Key**
   - Displays bar charts showing the average AC and DC power generated for each source key.

### 3. **Yield Analysis by Source Key**
   - Provides a bar chart showing the average daily yield and total yield for each source key.

### 4. **Time Series Analysis**
   - Displays a line chart of DC power generation over time, enabling users to observe trends and fluctuations in power output.

### 5. **Yield vs Ambient Temperature**
   - A scatter plot comparing daily yield with ambient temperature, helping to explore how temperature impacts solar energy production.

### 6. **Temperature Ranges and Yield**
   - A box plot illustrating how daily yield varies across different temperature ranges, helping identify optimal temperature conditions for solar power generation.

### 7. **Irradiation vs Power Output**
   - Scatter plots comparing irradiation levels with both AC and DC power output, enabling analysis of the relationship between solar irradiance and power generation.

### 8. **Total Yield Over Time**
   - A line chart showing the total yield over time, offering insights into long-term solar energy generation.

---

## Installation

To run the Solar Power Analysis Dashboard locally, follow these steps:

### Prerequisites:
Make sure you have Python 3.7+ installed on your system.

1. **Clone the repository:**

   git clone https://github.com/Anand99Nair/solar-power-analysis-dashboard.git
   cd solar-power-analysis-dashboard

2. **Install dependencies:**

You can use pip to install the required Python libraries:

    pip install -r requirements.txt

Alternatively, you can install the required packages individually:

    pip install streamlit pandas matplotlib seaborn plotly

3. **Place your data file:**

Ensure that the merged_data.csv file is placed in the root directory of the project. This file should contain the solar power data with columns such as DATE_TIME, SOURCE_KEY, DC_POWER, AC_POWER, DAILY_YIELD, TOTAL_YIELD, AMBIENT_TEMPERATURE, MODULE_TEMPERATURE, and IRRADIATION.

4. **Run the application:**

After installation, you can start the Streamlit app by running:

    streamlit run app.py

This will launch the application in your default web browser.

## Usage

1. **Sidebar Filters:**
    Select Source Keys: Choose one or more source keys from the dropdown list.
    Select Date Range: Choose a date range to filter the data.

2. **Dashboard Sections:**
    Correlation Heatmap: View the correlation between key metrics.
    Average AC and DC Power by Source Key: Visualize average power generation for each source key.
    Yield Analysis by Source Key: Compare daily and total yield across source keys.
    Time Series Analysis: Explore how DC power varies over time.
    Yield vs Ambient Temperature: Analyze the relationship between temperature and daily yield.
    Temperature Ranges and Yield: See how yield changes across different temperature ranges.
    Irradiation vs Power Output: Compare irradiation and power generation.
    Total Yield Over Time: Track the total yield generated over time.

## Technologies Used

    Streamlit: For building the interactive web application.
    Pandas: For data manipulation and processing.
    Plotly: For interactive visualizations.
    Matplotlib: For static visualizations (used in heatmap).
    Seaborn: For statistical data visualization (used in heatmap).

## Conclusion

The Solar Power Analysis Dashboard provides a powerful tool for exploring and analyzing solar power data. By offering various visualization options, it helps users to gain insights into factors affecting solar energy production, such as temperature, irradiation, and source key. The interactive nature of the application allows users to customize their analysis with filters for source keys and date ranges.

This project is ideal for anyone interested in solar energy data analysis, whether for research, optimization, or monitoring purposes.