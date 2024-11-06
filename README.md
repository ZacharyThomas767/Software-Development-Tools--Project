url:https://vehicle-data-dashboard-2zn6.onrender.com

Vehicle Price Analysis and Visualization Dashboard
This project is a web-based dashboard created using Streamlit, which allows users to explore and visualize vehicle price data. The application provides interactive charts and scatter plots to compare various vehicle categories and their average prices, as well as to explore relationships between numerical features.

Features
Compare Average Price by Category: Allows users to select two categorical columns to compare the average vehicle price across different categories.
Interactive Scatter Plot: Users can create scatter plots by selecting numerical columns for the X and Y axes, with options to overlay additional categorical data.
Month Filter: A month filter enables users to display data for specific months (from January to December).
Category Overlay: Users can toggle the visibility of various categories, such as make, model, or year, on the scatter plot for further analysis.
Installation
Prerequisites
Python 3.x
pip
Setup
Clone this repository or download the project files.

Install the necessary dependencies:

Create a virtual environment (optional, but recommended):

Copy code
python -m venv .env
Activate the virtual environment:
On Windows:

.\.env\Scripts\activate
On macOS/Linux:

source .env/bin/activate
Install required Python packages:


pip install -r requirements.txt
Place the dataset file (vehicles_us.csv) in the project directory. The dataset should contain columns such as price, make, model, year, date_posted, etc.

Usage
Run the Streamlit app:

streamlit run app.py
Open the application in your browser by navigating to the URL provided in the terminal (usually http://localhost:8501).

Explore the following interactive features:

Use the dropdowns to select columns and compare average prices.
Create scatter plots by selecting numerical columns and overlay category data.
Filter the data by months and toggle category visibility.
Dependencies
This project uses the following Python libraries:

streamlit: For building the web app.
pandas: For data manipulation and processing.
plotly: For creating interactive visualizations.
numpy: For numerical operations.
seaborn and matplotlib: Optional libraries for additional visualization options.
Requirements:
Python 3.x
Streamlit
Pandas
Plotly
NumPy
Seaborn (optional)
Matplotlib (optional)

licenced by me! 