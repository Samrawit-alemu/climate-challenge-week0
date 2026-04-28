import pandas as pd 
import streamlit as st
import plotly.express as px
from utils import load_data

st.set_page_config(page_title="African Climate Dashboard", layout="wide")

st.title("🌍 African Climate Trend Analysis (2015-2026)")
st.markdown("Interactive dashboard for COP32 policy planning.")

# Load Data
df = load_data()

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filters")

# 1. Country Selector
selected_countries = st.sidebar.multiselect(
    "Select Countries", 
    options=df['Country'].unique(), 
    default=df['Country'].unique()
)

# 2. Variable Selector
variable = st.sidebar.selectbox(
    "Select Variable", 
    options=['T2M', 'PRECTOTCORR', 'RH2M', 'WS2M'], 
    index=0
)

# 3. Year Range Slider
min_year = int(df['YEAR'].min())
max_year = int(df['YEAR'].max())
year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (2015, 2026))

# Filter Data based on selection
filtered_df = df[
    (df['Country'].isin(selected_countries)) & 
    (df['YEAR'] >= year_range[0]) & 
    (df['YEAR'] <= year_range[1])
]

# --- CHARTS ---
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"{variable} Trend Over Time")
    # Resample to monthly to make it smooth
    plot_df = filtered_df.groupby(['Country', pd.Grouper(key='Date', freq='ME')])[variable].mean().reset_index()
    fig_line = px.line(plot_df, x='Date', y=variable, color='Country', template="plotly_white")
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    st.subheader(f"Distribution of {variable}")
    fig_box = px.box(filtered_df, x='Country', y=variable, color='Country', points=False)
    # Use log scale for precipitation
    if variable == 'PRECTOTCORR':
        fig_box.update_layout(yaxis_type="log")
    st.plotly_chart(fig_box, use_container_width=True)

st.write("Data Source: NASA POWER Database")