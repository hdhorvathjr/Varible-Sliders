
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Interactive U.S. Economic Growth Projection")

st.markdown("Adjust sliders below to simulate 10-year projections for GDP, Revenue, and Profit.")

# Sliders for annual growth rates
gdp_growth = st.slider("Annual GDP Growth Rate (%)", 0.0, 10.0, 2.0)
revenue_growth = st.slider("Annual Revenue Growth Rate (%)", 0.0, 15.0, 5.0)
profit_growth = st.slider("Annual Profit Growth Rate (%)", 0.0, 20.0, 7.0)

# Initial values
start_year = 2025
years = list(range(start_year, start_year + 10))
gdp_base = 28000  # in billions (e.g., $28T)
revenue_base = 4000  # in billions
profit_base = 800  # in billions

# Calculate projections
gdp = [gdp_base * ((1 + gdp_growth / 100) ** i) for i in range(10)]
revenue = [revenue_base * ((1 + revenue_growth / 100) ** i) for i in range(10)]
profit = [profit_base * ((1 + profit_growth / 100) ** i) for i in range(10)]

df = pd.DataFrame({
    "Year": years,
    "GDP ($B)": gdp,
    "Revenue ($B)": revenue,
    "Profit ($B)": profit
})

# Melt dataframe for Altair
df_melt = df.melt('Year', var_name='Metric', value_name='Amount')

# Chart
chart = alt.Chart(df_melt).mark_line().encode(
    x='Year:O',
    y='Amount:Q',
    color='Metric:N'
).properties(
    width=700,
    height=400,
    title='U.S. Economic Projections (2025–2034)'
)

st.altair_chart(chart, use_container_width=True)
