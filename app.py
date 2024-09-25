import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px

from clean import load_and_clean_data


df = load_and_clean_data()

# Initialize the app
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Define the layout of the top navigation bar and the three tabs
app.layout = dbc.Container([
    # Navigation bar
    dbc.NavbarSimple(
        brand="Michelin Star Restaurant Guide",
        color="dark",
        dark=True,
        className="mb-4",
    ),
    
    # Tabs
    dcc.Tabs(id="tabs-example", value='overview-tab', children=[
        dcc.Tab(label='Overview', value='overview-tab'),
        dcc.Tab(label='Explore', value='explore-tab'),
        dcc.Tab(label='Create', value='create-tab'),
    ]),
    
    html.Div(id='tabs-content')
], fluid=True)


# Callbacks to switch between tabs
@app.callback(
    dash.dependencies.Output('tabs-content', 'children'),
    dash.dependencies.Input('tabs-example', 'value')
)
def render_content(tab):
    if tab == 'overview-tab':
        return overview_tab_content()
    elif tab == 'explore-tab':
        return explore_tab_content()
    elif tab == 'create-tab':
        return create_tab_content()


# Overview tab content
def overview_tab_content():
    # Example: Bar chart of number of restaurants by Michelin stars
    star_counts = df['Award'].value_counts()
    bar_fig = px.bar(star_counts, x=star_counts.index, y=star_counts.values,
                     labels={'x': 'Michelin Stars', 'y': 'Number of Restaurants'},
                     title="Distribution of Michelin Star Restaurants")
    
    # Example: Map of all restaurants
    map_fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", 
                                hover_name="Name", hover_data=["Cuisine", "Price", "Location"],
                                color="Award", zoom=2, height=500,
                                title="Michelin Star Restaurants Around the World")
    map_fig.update_layout(mapbox_style="open-street-map")
    
    return dbc.Container([
        html.H3("Overview of Michelin Star Restaurants"),
        dbc.Row([
            dbc.Col(dcc.Graph(figure=bar_fig), width=6),
            dbc.Col(dcc.Graph(figure=map_fig), width=6),
        ]),
    ])


# Explore tab content with filters
def explore_tab_content():

    df_cleaned = df.dropna(subset=['Cuisine', 'Location'])

    # Dropdown filters for location, cuisine, and stars
    location_options = [{'label': loc, 'value': loc} for loc in df['Location'].unique()]
    # Ensure there are no NaN or empty values in the Cuisine column
    df['Cuisine'] = df['Cuisine'].fillna('Unknown')

    # Remove any trailing commas or unwanted characters from cuisine values
    df['Cuisine'] = df['Cuisine'].str.strip()

    # Generate cuisine options for the dropdown
    cuisine_options = [{'label': cuisine, 'value': cuisine} for cuisine in df['Cuisine'].unique() if cuisine]

        
    award_options = [{'label': star, 'value': star} for star in df['Award'].unique()]

    return dbc.Container([
        html.H3("Explore Michelin Star Restaurants"),
        dbc.Row([
            dbc.Col(dcc.Dropdown(id='location-filter', options=location_options, 
                                 placeholder="Select a Location"), width=4),
            dbc.Col(dcc.Dropdown(id='cuisine-filter', options=cuisine_options, 
                                 placeholder="Select a Cuisine"), width=4),
            dbc.Col(dcc.Dropdown(id='award-filter', options=award_options, 
                                 placeholder="Select Michelin Stars"), width=4),
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='filtered-map'), width=12)
        ])
    ])


# Create tab content (leave for your own customization)
def create_tab_content():
    return dbc.Container([
        html.H3("Create Your Michelin Restaurant Road Trip"),
        html.P("This tab will allow users to create a road trip based on selected restaurants and criteria."),
    ])


# Callback for updating the map based on filters (Explore tab)
@app.callback(
    dash.dependencies.Output('filtered-map', 'figure'),
    [
        dash.dependencies.Input('location-filter', 'value'),
        dash.dependencies.Input('cuisine-filter', 'value'),
        dash.dependencies.Input('award-filter', 'value')
    ]
)
def update_map(location, cuisine, award):
    # Filter the dataframe based on the selected criteria
    filtered_df = df.copy()
    if location:
        filtered_df = filtered_df[filtered_df['Location'] == location]
    if cuisine:
        filtered_df = filtered_df[filtered_df['Cuisine'] == cuisine]
    if award:
        filtered_df = filtered_df[filtered_df['Award'] == award]
    
    # Create a new map with the filtered data
    fig = px.scatter_mapbox(filtered_df, lat="Latitude", lon="Longitude", 
                            hover_name="Name", hover_data=["Cuisine", "Price", "Location"],
                            color="Award", zoom=2, height=500,
                            title="Filtered Michelin Star Restaurants")
    fig.update_layout(mapbox_style="open-street-map")
    return fig

    

if __name__ == '__main__':
    app.run_server(debug=True)
