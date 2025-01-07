import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

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
"""
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

"""
# Set common chart styling parameters
chart_height = 300
border_color = "rgba(0,0,0,0.1)"
bg_color = "white"
text_color = "rgba(0,0,0,0.7)"

# Update each chart with new styling
figures = {
    'demographics': px.pie(data_gender_age, names='Category', values='Percentage',
                         title="Demographics Overview", height=chart_height,
                         color_discrete_sequence=px.colors.sequential.RdBu)
    .update_layout(
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        title_font=dict(size=18, color=text_color),
        margin=dict(l=20, r=20, t=40, b=20),
        showlegend=True,
        legend_title=dict(text="Categories", font=dict(size=12, color=text_color)),
        margin_pad=10,
        font=dict(size=14, color=text_color)
    )
    .update_traces(marker=dict(line=dict(color=border_color, width=1))),

    'water_availability': px.bar(data_water_availability, x="Category", y="Respondents",
                               color="Year", barmode="group", title="Water Availability Changes",
                               height=chart_height, color_discrete_sequence=px.colors.qualitative.Set1)
    .update_layout(
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        title_font=dict(size=18, color=text_color),
        xaxis_title="Category",
        yaxis_title="Respondents",
        margin=dict(l=30, r=30, t=40, b=30),
        showlegend=True,
        font=dict(size=14, color=text_color)
    )
    .update_traces(marker=dict(line=dict(color=border_color, width=1))),

    'agri_water': px.line(data_agri_water.melt(id_vars="Year", var_name="Condition", value_name="Percentage"),
                         x="Year", y="Percentage", color="Condition", title="Agricultural Water Availability",
                         height=chart_height, color_discrete_sequence=px.colors.qualitative.Dark2)
    .update_layout(
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        title_font=dict(size=18, color=text_color),
        xaxis_title="Year",
        yaxis_title="Percentage",
        margin=dict(l=30, r=30, t=40, b=30),
        showlegend=True,
        font=dict(size=14, color=text_color)
    )
    .update_traces(line=dict(width=2, color=border_color)),

    'irrigation': px.bar(data_irrigation, x="Practice", y="Percentage",
                       title="Change in Irrigation Practices", height=chart_height,
                       color_discrete_sequence=px.colors.sequential.Viridis)
    .update_layout(
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        title_font=dict(size=18, color=text_color),
        xaxis_title="Practice",
        yaxis_title="Percentage",
        margin=dict(l=30, r=30, t=40, b=30),
        showlegend=True,
        font=dict(size=14, color=text_color)
    )
    .update_traces(marker=dict(line=dict(color=border_color, width=1))),

    'crop_types': px.bar(data_crop_types, x="Crop", y="Percentage", color="Year", barmode="group",
                        title="Crop Types (2021 vs. 2024)", height=chart_height, 
                        color_discrete_sequence=px.colors.qualitative.Plotly)
    .update_layout(
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        title_font=dict(size=18, color=text_color),
        xaxis_title="Crop",
        yaxis_title="Percentage",
        margin=dict(l=30, r=30, t=40, b=30),
        showlegend=True,
        font=dict(size=14, color=text_color)
    )
    .update_traces(marker=dict(line=dict(color=border_color, width=1))),

    'yield_changes': px.bar(data_yield_changes, x="Category", y="Percentage", orientation="h",
                           title="Yield Changes", height=chart_height, 
                           color_discrete_sequence=px.colors.sequential.Blues)
    .update_layout(
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        title_font=dict(size=18, color=text_color),
        xaxis_title="Percentage",
        yaxis_title="Category",
        margin=dict(l=30, r=30, t=40, b=30),
        showlegend=True,
        font=dict(size=14, color=text_color)
    )
    .update_traces(marker=dict(line=dict(color=border_color, width=1))),

    'income': px.area(data_income.melt(id_vars="Year", var_name="Income Level", value_name="Percentage"),
                     x="Year", y="Percentage", color="Income Level", title="Income Changes Over Time",
                     height=chart_height, color_discrete_sequence=px.colors.sequential.Sunset)
    .update_layout(
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        title_font=dict(size=18, color=text_color),
        xaxis_title="Year",
        yaxis_title="Percentage",
        margin=dict(l=30, r=30, t=40, b=30),
        showlegend=True,
        font=dict(size=14, color=text_color)
    )
    .update_traces(line=dict(width=2, color=border_color)),

    'economic': px.pie(data_economic.iloc[:2], names="Activity", values="Percentage", 
                       title="Economic Activities", height=chart_height, 
                       color_discrete_sequence=px.colors.sequential.Emrld)
    .update_layout(
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        title_font=dict(size=18, color=text_color),
        margin=dict(l=20, r=20, t=40, b=20),
        showlegend=True,
        legend_title=dict(text="Economic Activities", font=dict(size=12, color=text_color)),
        font=dict(size=14, color=text_color)
    )
    .update_traces(marker=dict(line=dict(color=border_color, width=1))),

    'employment': px.bar(data_economic.iloc[2:], x="Activity", y="Percentage", 
                         title="Employment Opportunities", height=chart_height,
                         color_discrete_sequence=px.colors.qualitative.Set3)
    .update_layout(
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        title_font=dict(size=18, color=text_color),
        xaxis_title="Activity",
        yaxis_title="Percentage",
        margin=dict(l=30, r=30, t=40, b=30),
        showlegend=True,
        font=dict(size=14, color=text_color)
    )
    .update_traces(marker=dict(line=dict(color=border_color, width=1))),

    'wellbeing': px.bar(data_wellbeing.melt(id_vars="Year", var_name="Rating", value_name="Percentage"),
                        x="Year", y="Percentage", color="Rating", barmode="group", 
                        title="Well-being Ratings", height=chart_height, 
                        color_discrete_sequence=px.colors.qualitative.T10)
    .update_layout(
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        title_font=dict(size=18, color=text_color),
        xaxis_title="Year",
        yaxis_title="Percentage",
        margin=dict(l=30, r=30, t=40, b=30),
        showlegend=True,
        font=dict(size=14, color=text_color)
    )
    .update_traces(marker=dict(line=dict(color=border_color, width=1))),

    'community': px.bar(data_community, x="Improvement", y="Percentage", orientation="h",
                        title="Community Benefits", height=chart_height, 
                        color_discrete_sequence=px.colors.sequential.Mint)
    .update_layout(
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        title_font=dict(size=18, color=text_color),
        xaxis_title="Percentage",
        yaxis_title="Improvement",
        margin=dict(l=30, r=30, t=40, b=30),
        showlegend=True,
        font=dict(size=14, color=text_color)
    )
    .update_traces(marker=dict(line=dict(color=border_color, width=1))),

    'benefits': px.pie(data_benefits, names="Category", values="Percentage", 
                       title="Significant Benefits", height=chart_height,
                       color_discrete_sequence=px.colors.qualitative.Bold)
    .update_layout(
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        title_font=dict(size=18, color=text_color),
        margin=dict(l=20, r=20, t=40, b=20),
        showlegend=True,
        legend_title=dict(text="Benefits", font=dict(size=12, color=text_color)),
        font=dict(size=14, color=text_color)
    )
    .update_traces(marker=dict(line=dict(color=border_color, width=1))),

    'suggestions': px.bar(data_suggestions, x="Suggestion", y="Frequency", 
                          title="Suggestions Distribution", height=chart_height,
                          color_discrete_sequence=px.colors.qualitative.Safe)
    .update_layout(
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        title_font=dict(size=18, color=text_color),
        xaxis_title="Suggestion",
        yaxis_title="Frequency",
        margin=dict(l=30, r=30, t=40, b=30),
        showlegend=True,
        font=dict(size=14, color=text_color)
    )
    .update_traces(marker=dict(line=dict(color=border_color, width=1))),
}

# Define the layout of the app
app.layout = html.Div([
    html.Div([
        html.Div([
            html.H2("Dashboard", style={'color': 'white', 'text-align': 'center'}),
            html.Hr(style={'border': '1px solid #ccc'}),
            html.Div([
                html.Button("Demograph", id="demograph-btn", n_clicks=0, className="sidebar-button"),
                html.Button("Household Water Improvement", id="household-water-btn", n_clicks=0, className="sidebar-button"),
                html.Button("Agriculture and Irrigation Water Improvement", id="agriculture-water-btn", n_clicks=0, className="sidebar-button"),
                html.Button("Yield from Agriculture", id="yield-btn", n_clicks=0, className="sidebar-button"),
                html.Button("Crops", id="crops-btn", n_clicks=0, className="sidebar-button"),
                html.Button("Economic Growth", id="economic-growth-btn", n_clicks=0, className="sidebar-button"),
                html.Button("Livestock", id="livestock-btn", n_clicks=0, className="sidebar-button"),
                html.Button("Well-being and Community Benefits", id="well-being-btn", n_clicks=0, className="sidebar-button"),
                html.Button("Suggestions", id="suggestions-btn", n_clicks=0, className="sidebar-button"),
            ], style={'display': 'flex', 'flexDirection': 'column'}),
        ], id="sidebar", style={
            'width': '20%', 'height': '100%', 'position': 'fixed', 'top': '0', 'left': '0',
            'background-color': '#2c3e50', 'padding': '20px', 'color': 'white'
        }),

        # Main Content Area
        html.Div(id="content", style={'margin-left': '20%', 'padding': '20px', 'background-color': '#ecf0f1'})
    ], style={'display': 'flex'}),
])

# Define the callback to update the content based on button clicks
@app.callback(
    Output('content', 'children'),
    Input('demograph-btn', 'n_clicks'),
    Input('household-water-btn', 'n_clicks'),
    Input('agriculture-water-btn', 'n_clicks'),
    Input('yield-btn', 'n_clicks'),
    Input('crops-btn', 'n_clicks'),
    Input('economic-growth-btn', 'n_clicks'),
    Input('livestock-btn', 'n_clicks'),
    Input('well-being-btn', 'n_clicks'),
    Input('suggestions-btn', 'n_clicks')
)
def update_content(demograph_clicks, household_water_clicks, agriculture_water_clicks,
                   yield_clicks, crops_clicks, economic_growth_clicks, livestock_clicks, 
                   well_being_clicks, suggestions_clicks):
    ctx = dash.callback_context

    if not ctx.triggered:
        return html.Div(["Welcome to the Dashboard!"])

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'demograph-btn':
        return dcc.Graph(figure=figures['demographics'])
    elif button_id == 'household-water-btn':
        return dcc.Graph(figure=figures['water_availability'])
    elif button_id == 'agriculture-water-btn':
        return dcc.Graph(figure=figures['agri_water'])
    elif button_id == 'yield-btn':
        return dcc.Graph(figure=figures['yield_changes'])
    elif button_id == 'crops-btn':
        return dcc.Graph(figure=figures['crop_types'])
    elif button_id == 'economic-growth-btn':
        return dcc.Graph(figure=figures['economic'])
    elif button_id == 'livestock-btn':
        return dcc.Graph(figure=figures['employment'])
    elif button_id == 'well-being-btn':
        return dcc.Graph(figure=figures['wellbeing'])
    elif button_id == 'suggestions-btn':
        return dcc.Graph(figure=figures['suggestions'])
    else:
        return html.Div([
            html.H3("Other Section", style={'text-align': 'center'}),
            html.P("This is where the content for other sections will appear.", style={'text-align': 'center'}),
        ])

if __name__ == "__main__":
    app.run_server(debug=True)
