
 #Dependencies Libraries
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from flask import Flask
import dash_bootstrap_components as dbc

# Initialize Flask server
server = Flask(__name__)

# Initialize Dash app with Bootstrap theme
app = Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create all datasets
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
    "Activity": ["New Businesses", "No Change", "Fewer Jobs", "Same Jobs", "More Jobs"],
    "Percentage": [40, 60, 10, 30, 60]
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

# Create figures with consistent height
chart_height = 300

figures = {
    'demographics': px.pie(data_gender_age, names='Category', values='Percentage',
                         title="Demographics Overview", height=chart_height,
                         color_discrete_sequence=px.colors.sequential.RdBu),
    
    'water_availability': px.bar(data_water_availability, x="Category", y="Respondents",
                               color="Year", barmode="group", title="Water Availability Changes",
                               height=chart_height, color_discrete_sequence=px.colors.qualitative.Set1),
    
    'agri_water': px.line(data_agri_water.melt(id_vars="Year", var_name="Condition",
                         value_name="Percentage"), x="Year", y="Percentage",
                         color="Condition", title="Agricultural Water Availability",
                         height=chart_height, color_discrete_sequence=px.colors.qualitative.Dark2),
    
    'irrigation': px.bar(data_irrigation, x="Practice", y="Percentage",
                       title="Change in Irrigation Practices", height=chart_height,
                       color_discrete_sequence=px.colors.sequential.Viridis),
    
    'crop_types': px.bar(data_crop_types, x="Crop", y="Percentage",
                        color="Year", barmode="group", title="Crop Types (2021 vs. 2024)",
                        height=chart_height, color_discrete_sequence=px.colors.qualitative.Plotly),
    
    'yield_changes': px.bar(data_yield_changes, x="Category", y="Percentage",
                           orientation="h", title="Yield Changes", height=chart_height,
                           color_discrete_sequence=px.colors.sequential.Blues),
    
    'income': px.area(data_income.melt(id_vars="Year", var_name="Income Level",
                     value_name="Percentage"), x="Year", y="Percentage",
                     color="Income Level", title="Income Changes Over Time",
                     height=chart_height, color_discrete_sequence=px.colors.sequential.Sunset),
    
    'economic': px.pie(data_economic.iloc[:2], names="Activity",
                      values="Percentage", title="Economic Activities",
                      height=chart_height, color_discrete_sequence=px.colors.sequential.Emrld),
    
    'employment': px.bar(data_economic.iloc[2:], x="Activity", y="Percentage",
                       title="Employment Opportunities", height=chart_height,
                       color_discrete_sequence=px.colors.qualitative.Set3),
    
    'wellbeing': px.bar(data_wellbeing.melt(id_vars="Year", var_name="Rating",
                       value_name="Percentage"), x="Year", y="Percentage",
                       color="Rating", barmode="group", title="Well-being Ratings",
                       height=chart_height, color_discrete_sequence=px.colors.qualitative.T10),
    
    'community': px.bar(data_community, x="Improvement", y="Percentage",
                      orientation="h", title="Community Benefits",
                      height=chart_height, color_discrete_sequence=px.colors.sequential.Mint),
    
    'benefits': px.pie(data_benefits, names="Category", values="Percentage",
                      title="Significant Benefits", height=chart_height,
                      color_discrete_sequence=px.colors.qualitative.Bold),
    
    'suggestions': px.bar(data_suggestions, x="Suggestion", y="Frequency",
                        title="Suggestions Distribution", height=chart_height,
                        color_discrete_sequence=px.colors.qualitative.Safe)
}

# Update layout for all figures
for fig in figures.values():
    fig.update_layout(
        margin=dict(l=10, r=10, t=40, b=20),
        plot_bgcolor='white',
        paper_bgcolor='white'
    )

# Layout
app.layout = html.Div([
    # Header
    html.Div([
        html.H1("Alkod Lake Dashboard", className="dashboard-header"),
        html.P("Comprehensive analysis of lake impact on community and environment", className="dashboard-subtitle"),
    ], className="header-container"),
    
    # Main content
    html.Div([
        dbc.Row([
            # Key Metrics Section
            dbc.Col(dcc.Graph(figure=figures['demographics']), md=4),
            dbc.Col(dcc.Graph(figure=figures['water_availability']), md=4),
            dbc.Col(dcc.Graph(figure=figures['agri_water']), md=4),
        ], className="mb-4"),
        
        # Agricultural Section
        dbc.Row([
            dbc.Col(dcc.Graph(figure=figures['irrigation']), md=4),
            dbc.Col(dcc.Graph(figure=figures['crop_types']), md=4),
            dbc.Col(dcc.Graph(figure=figures['yield_changes']), md=4),
        ], className="mb-4"),
        
        # Economic Section
        dbc.Row([
            dbc.Col(dcc.Graph(figure=figures['income']), md=4),
            dbc.Col(dcc.Graph(figure=figures['economic']), md=4),
            dbc.Col(dcc.Graph(figure=figures['employment']), md=4),
        ], className="mb-4"),
        
        # Community Section
        dbc.Row([
            dbc.Col(dcc.Graph(figure=figures['wellbeing']), md=4),
            dbc.Col(dcc.Graph(figure=figures['community']), md=4),
            dbc.Col(dcc.Graph(figure=figures['benefits']), md=4),
        ], className="mb-4"),
        
        # Feedback Section
        dbc.Row([
            dbc.Col(dcc.Graph(figure=figures['suggestions']), md=12),
        ], className="mb-4"),
    ], className="dashboard-content")
])

# Add custom styles
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Alkod Lake Dashboard</title>
        {%favicon%}
        {%css%}
        <style>
            body {
                background-color: #f8f9fa;
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            
            .header-container {
                background-color: #2c3e50;
                color: white;
                padding: 2rem;
                text-align: center;
                margin-bottom: 2rem;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            
            .dashboard-header {
                margin: 0;
                font-size: 2.5rem;
                font-weight: 600;
            }
            
            .dashboard-subtitle {
                margin: 0.5rem 0 0 0;
                font-size: 1.1rem;
                opacity: 0.9;
            }
            
            .dashboard-content {
                padding: 0 2rem 2rem 2rem;
            }
            
            .mb-4 {
                margin-bottom: 2rem;
            }
            
            .chart-container {
                background: white;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
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