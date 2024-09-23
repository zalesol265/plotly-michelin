import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from clean import load_and_clean_data


df = load_and_clean_data()

# Initialize the app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Michelin Star Restaurants"),
    
    dcc.Dropdown(
        id='cuisine-filter',
        options=[{'label': cuisine, 'value': cuisine} for cuisine in df['Cuisine'].unique()],
        placeholder="Select a cuisine",
        multi=True
    ),
    
    dcc.Graph(id='michelin-map'),

    # A second graph to show insights (e.g., Michelin Stars per country or cuisine)
    dcc.Graph(id='insight-chart')
])

# Callbacks to update the map and chart based on filters
@app.callback(
    Output('michelin-map', 'figure'),
    Input('cuisine-filter', 'value')
)
def update_map(selected_cuisines):
    filtered_df = df[df['Cuisine'].isin(selected_cuisines)] if selected_cuisines else df
    
    fig = px.scatter_mapbox(
        filtered_df,
        lat='Latitude',
        lon='Longitude',
        hover_name='Name',
        hover_data={'Cuisine': True, 'Price': True, 'Award': True},
        color='Award',  # Color points based on Michelin star count
        zoom=3,
        height=600
    )
    fig.update_layout(mapbox_style="open-street-map")
    return fig


    

if __name__ == '__main__':
    app.run_server(debug=True)
