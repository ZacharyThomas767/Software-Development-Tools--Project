import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# reading data
vehicles = pd.read_csv('vehicles_us.csv')

# Setting categorical and nemarical columns
categorical_cols = vehicles.select_dtypes(include='object').columns
numerical_cols = vehicles.select_dtypes(include=np.number).columns

#comparing 2 graphs displaying price vs columns

# Add dropdowns for selecting columns
st.header("Compare Average Price by Category")
col1 = st.selectbox("Select first column", options=categorical_cols, index=0)
col2 = st.selectbox("Select second column", options=categorical_cols, index=1)

# Function to create average price plot for a given column
def plot_average_price_by_column(column, plot_width=800, plot_height=500):
    # Calculate average price for each category in the selected column
    average_price = vehicles.groupby(column)['price'].mean().dropna().sort_values(ascending=False).reset_index()

    # Create a Plotly bar chart with larger dimensions
    fig = px.bar(
        average_price,
        x=column,
        y="price",
        title=f"Average Price by {column}",
        labels={column: column, "price": "Average Price"},
        color_discrete_sequence=px.colors.sequential.Viridis,
        width=plot_width,
        height=plot_height
    )
    fig.update_layout(xaxis_title=column, yaxis_title="Average Price", xaxis_tickangle=45)
    return fig

# Display the two selected plots side by side with specified dimensions
col1_fig = plot_average_price_by_column(col1)
col2_fig = plot_average_price_by_column(col2)

# Use Streamlit's columns to place the plots side by side
col1, col2 = st.columns([1, 1])
col1.plotly_chart(col1_fig, use_container_width=False)
col2.plotly_chart(col2_fig, use_container_width=False)

# Convert date_posted to datetime if not already in datetime format
vehicles["date_posted"] = pd.to_datetime(vehicles["date_posted"], errors="coerce")



# Scatter plot setup
st.header("Interactive Scatter Plot")

# Create layout with two columns
left_column, right_column = st.columns([3, 1])

# Scatter plot controls (in the left column)
with left_column:
    # Select numerical columns for x and y axes
    x_axis = st.selectbox("Select X-axis", options=numerical_cols)
    y_axis = st.selectbox("Select Y-axis", options=numerical_cols)
    
    # Add submit button to control when the plot updates
    update_plot = st.button("Submit")

# Choices for plotting only when the "Submit" button is clicked
overlay_options = {}

# Options in the right column (checkboxes)
with right_column:
    # Define the correct order of months
    month_order = ["January", "February", "March", "April", "May", "June", 
                   "July", "August", "September", "October", "November", "December"]
    
    # Add checkboxes for each month in the defined order
    st.subheader("Select Months to Display")
    month_selected = []
    for month in month_order:
        if month in vehicles["date_posted"].dt.month_name().unique():  # Check if month is present in data
            if st.checkbox(month, value=True):  # Default checked
                month_selected.append(month)

    st.subheader("Overlay and Toggle Visibility for Categories")
    for col in categorical_cols:
        if col != "date_posted":  # Exclude the exact date option
            if st.checkbox(f"Overlay by {col}"):
                unique_values = vehicles[col].unique()
                for value in unique_values:
                    visibility = st.checkbox(f"Show {col} - {value}", value=True, key=f"{col}_{value}")
                    overlay_options[(col, value)] = visibility

# Base scatter plot (updated only on submit)
if update_plot:
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=vehicles[x_axis],
            y=vehicles[y_axis],
            mode="markers",
            marker=dict(color="grey", opacity=0.5),
            name="Base Data",
        )
    )

    # Filter data by selected months
    if month_selected:
        month_filtered_data = vehicles[vehicles["date_posted"].dt.month_name().isin(month_selected)]
    else:
        month_filtered_data = vehicles  # If no month selected, show all data

    # Add overlays based on selected categories and checkbox visibility
    for (col, value), visibility in overlay_options.items():
        if visibility:
            filtered_data = month_filtered_data[month_filtered_data[col] == value]
            fig.add_trace(
                go.Scatter(
                    x=filtered_data[x_axis],
                    y=filtered_data[y_axis],
                    mode="markers",
                    marker=dict(opacity=0.7),
                    name=f"{col}: {value}",
                    legendgroup=col,
                )
            )

    fig.update_layout(
        title=f"{y_axis} vs {x_axis} with Category Overlays",
        xaxis_title=x_axis,
        yaxis_title=y_axis,
        showlegend=True,
    )

    with left_column:
        st.plotly_chart(fig)
