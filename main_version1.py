from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from flask import Flask
import dash_bootstrap_components as dbc

# Initialize Flask server
server = Flask(__name__)

# Initialize Dash app with Bootstrap theme
app = Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create the DataFrames
data_gender_age = pd.DataFrame({
    "Category": ["Female", "Male", "Age 46-60", "Age 30-45", "Other"],
    "Percentage": [50, 40, 60, 30, 10]
})

data_water_availability = pd.DataFrame({
    "Year": ["2021", "2021", "2024", "2024"],
    "Category": ["Shortages", "Improved", "Shortages", "Improved"],
    "Respondents": [55, 20, 15, 60]
})

data_agri_water = pd.DataFrame({
    "Year": ["2021", "2024"],
    "Shortages": [80, 20],
    "Improved": [20, 80]
})

data_irrigation = pd.DataFrame({
    "Practice": ["Improved", "No Change", "Others"],
    "Percentage": [60, 25, 15]
})

data_crop_types = pd.DataFrame({
    "Year": ["2021", "2024", "2021", "2024"],
    "Crop": ["Mixed Cropping", "Mixed Cropping", "Cotton", "Cotton"],
    "Percentage": [45, 55, 55, 45]
})

data_yield_changes = pd.DataFrame({
    "Category": ["10-20%", "20-30%", ">30%"],
    "Percentage": [40, 35, 25]
})

data_income = pd.DataFrame({
    "Year": ["2021", "2024"],
    "Low": [70, 40],
    "Moderate": [20, 40],
    "Significant": [10, 20]
})

data_economic = pd.DataFrame({
    "Activity": ["New Businesses", "No Change"],
    "Percentage": [40, 60]
})

data_employment = pd.DataFrame({
    "Activity": ["Fewer Jobs", "Same Jobs", "More Jobs"],
    "Percentage": [10, 30, 60]
})

data_wellbeing = pd.DataFrame({
    "Year": ["2021", "2024"],
    "Poor": [50, 15],
    "Better": [30, 55],
    "Much Better": [20, 30]
})

data_community = pd.DataFrame({
    "Improvement": ["Access to Water", "Crop Productivity", "Others"],
    "Percentage": [55, 35, 10]
})

data_benefits = pd.DataFrame({
    "Category": ["Increased Productivity", "Others"],
    "Percentage": [75, 25]
})

data_suggestions = pd.DataFrame({
    "Suggestion": ["Storage of Water", "Maintain Lake", "Others", "New Initiatives"],
    "Frequency": [40, 30, 20, 10]
})

# Create summary cards data
def create_summary_stats():
    return [
        {"title": "Water Improvement", "value": "60%", "change": "+40%"},
        {"title": "Agricultural Growth", "value": "55%", "change": "+25%"},
        {"title": "Community Impact", "value": "75%", "change": "+45%"},
        {"title": "Economic Growth", "value": "40%", "change": "+30%"}
    ]

# Layout
app.layout = html.Div([
    # Sidebar
    html.Div([
        html.H2("Alkod Lake", className="sidebar-header"),
        html.H3("Dashboard", className="sidebar-subheader"),
        html.Hr(),
        dbc.Nav([
            dbc.NavLink("Overview", href="#overview", active="exact"),
            dbc.NavLink("Water Resources", href="#water", active="exact"),
            dbc.NavLink("Agriculture", href="#agriculture", active="exact"),
            dbc.NavLink("Economic Impact", href="#economic", active="exact"),
            dbc.NavLink("Community", href="#community", active="exact"),
            dbc.NavLink("Feedback", href="#feedback", active="exact"),
        ], vertical=True, pills=True),
    ], className="sidebar"),
    
    # Main content
    html.Div([
        # Summary Cards
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4(stat["title"], className="card-title"),
                        html.H2(stat["value"], className="card-value"),
                        html.P(f"YoY Change: {stat['change']}", className="card-change"),
                    ])
                ], className="summary-card")
            ], width=3) for stat in create_summary_stats()
        ], className="mb-4"),

        # Overview Section
        html.Div([
            html.H2("Overview", id="overview", className="section-header"),
            dbc.Row([
                dbc.Col(dcc.Graph(
                    figure=px.pie(data_gender_age, names='Category', values='Percentage',
                                title="Demographics Overview",
                                color_discrete_sequence=px.colors.sequential.RdBu)
                ), md=6),
                dbc.Col(dcc.Graph(
                    figure=px.bar(data_water_availability, x="Category", y="Respondents",
                                color="Year", barmode="group", title="Water Availability Changes",
                                color_discrete_sequence=px.colors.qualitative.Set1)
                ), md=6),
            ]),
        ], className="section"),

        # Water Resources Section
        html.Div([
            html.H2("Water Resources", id="water", className="section-header"),
            dbc.Row([
                dbc.Col(dcc.Graph(
                    figure=px.line(data_agri_water.melt(id_vars="Year", var_name="Condition", 
                                                       value_name="Percentage"),
                                 x="Year", y="Percentage", color="Condition",
                                 title="Agricultural Water Availability",
                                 color_discrete_sequence=px.colors.qualitative.Dark2)
                ), md=12),
            ]),
        ], className="section"),

        # Agriculture Section
        html.Div([
            html.H2("Agriculture", id="agriculture", className="section-header"),
            dbc.Row([
                dbc.Col(dcc.Graph(
                    figure=px.bar(data_irrigation, x="Practice", y="Percentage",
                                title="Irrigation Practices",
                                color_discrete_sequence=px.colors.sequential.Viridis)
                ), md=6),
                dbc.Col(dcc.Graph(
                    figure=px.bar(data_crop_types, x="Crop", y="Percentage",
                                color="Year", barmode="group",
                                title="Crop Types (2021 vs. 2024)",
                                color_discrete_sequence=px.colors.qualitative.Plotly)
                ), md=6),
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(
                    figure=px.bar(data_yield_changes, x="Category", y="Percentage",
                                orientation="h", title="Yield Changes",
                                color_discrete_sequence=px.colors.sequential.Blues)
                ), md=12),
            ]),
        ], className="section"),

        # Economic Impact Section
        html.Div([
            html.H2("Economic Impact", id="economic", className="section-header"),
            dbc.Row([
                dbc.Col(dcc.Graph(
                    figure=px.area(data_income.melt(id_vars="Year", var_name="Income Level",
                                                  value_name="Percentage"),
                                 x="Year", y="Percentage", color="Income Level",
                                 title="Income Changes Over Time",
                                 color_discrete_sequence=px.colors.sequential.Sunset)
                ), md=12),
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(
                    figure=px.pie(data_economic, names="Activity", values="Percentage",
                                title="Economic Activities",
                                color_discrete_sequence=px.colors.sequential.Emrld)
                ), md=6),
                dbc.Col(dcc.Graph(
                    figure=px.bar(data_employment, x="Activity", y="Percentage",
                                title="Employment Opportunities",
                                color_discrete_sequence=px.colors.qualitative.Set3)
                ), md=6),
            ]),
        ], className="section"),

        # Community Impact Section
        html.Div([
            html.H2("Community Impact", id="community", className="section-header"),
            dbc.Row([
                dbc.Col(dcc.Graph(
                    figure=px.bar(data_wellbeing.melt(id_vars="Year", var_name="Rating",
                                                     value_name="Percentage"),
                                x="Year", y="Percentage", color="Rating", barmode="group",
                                title="Well-being Ratings Over Time",
                                color_discrete_sequence=px.colors.qualitative.T10)
                ), md=12),
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(
                    figure=px.bar(data_community, x="Improvement", y="Percentage",
                                orientation="h",
                                title="Community Benefits from Lake Rejuvenation",
                                color_discrete_sequence=px.colors.sequential.Mint)
                ), md=6),
                dbc.Col(dcc.Graph(
                    figure=px.pie(data_benefits, names="Category", values="Percentage",
                                title="Significant Benefits",
                                color_discrete_sequence=px.colors.qualitative.Bold)
                ), md=6),
            ]),
        ], className="section"),

        # Feedback Section
        html.Div([
            html.H2("Feedback & Suggestions", id="feedback", className="section-header"),
            dbc.Row([
                dbc.Col(dcc.Graph(
                    figure=px.bar(data_suggestions, x="Suggestion", y="Frequency",
                                title="Suggestions Distribution",
                                color_discrete_sequence=px.colors.qualitative.Safe)
                ), md=12),
            ]),
        ], className="section"),
    ], className="main-content"),
])

# Custom CSS
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Alkod Lake Dashboard</title>
        {%favicon%}
        {%css%}
        <style>
            :root {
                --sidebar-width: 260px;
                --primary-color: #2c3e50;
                --secondary-color: #3498db;
            }
            
            body {
                background-color: #f8f9fa;
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            
            .sidebar {
                position: fixed;
                top: 0;
                left: 0;
                bottom: 0;
                width: var(--sidebar-width);
                padding: 2rem;
                background-color: var(--primary-color);
                color: white;
                overflow-y: auto;
                box-shadow: 2px 0 5px rgba(0,0,0,0.1);
            }
            
            .sidebar-header {
                color: white;
                font-size: 2rem;
                margin-bottom: 0;
                font-weight: 600;
            }
            
            .sidebar-subheader {
                color: var(--secondary-color);
                font-size: 1.5rem;
                margin-top: 0;
                margin-bottom: 1.5rem;
            }
            
            .main-content {
                margin-left: var(--sidebar-width);
                padding: 2rem;
                background-color: #f8f9fa;
                min-height: 100vh;
            }
            
            .section {
                margin-bottom: 3rem;
                padding: 2rem;
                background-color: white;
                border-radius: 12px;
                box-shadow: 0 2px 12px rgba(0,0,0,0.1);
            }
            
            .section-header {
                color: var(--primary-color);
                margin-bottom: 1.5rem;
                padding-bottom: 0.5rem;
                border-bottom: 2px solid #e9ecef;
            }
            
            .nav-link {
                color: #ecf0f1 !important;
                margin-bottom: 0.5rem;
                border-radius: 6px;
                transition: all 0.3s ease;
            }
            
            .nav-link:hover {
                background-color: rgba(52, 152, 219, 0.3) !important;
                transform: translateX(5px);
            }
            
            .nav-link.active {
                background-color: var(--secondary-color) !important;
                font-weight: 600;
            }
            
            .summary-card {
                border-radius: 10px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                transition: transform 0.3s ease;
            }
            
            .summary-card:hover {
                transform: translateY(-5px);
            }
            
            .card-title {
                color: var(--primary-color);
                font-size: 1rem;
                font-weight: 600;
            }
            
            .card-value {
                color: var(--secondary-color);
                font-size: 2rem;
                font-weight: 700;
                margin: 0.5rem 0;
            }
            
            .card-change {
                color: #27ae60;
                font-weight: 500;
                margin: 0;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

if __name__ == '__main__':
    app.run_server(debug=True)