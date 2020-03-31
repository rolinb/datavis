import plotly.graph_objects as go
import pandas as pd

#df2 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')
df = pd.read_csv('moredata.csv', sep='\t', header=0)
fig = go.Figure(data=go.Choropleth(
    locations = df['CODE'],
    z = df['Happiness score'],
    text = df['Country'],
    colorscale = 'icefire',
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_title = 'Happiness Score',
))

fig.update_layout(
    title_text='2019 Happiness Scores',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    
)


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()
app.layout = html.Div([
     dcc.RadioItems(
        options=[
            {'label': 'Happiness Rank', 'value':0},
            {'label': 'GDP Log', 'value':1},
            {'label': 'Freedom', 'value':2},
            {'label': 'Generosity', 'value':3},
            {'label': 'Social Support', 'value':4},
        ],
        value=0,
        id='radio-buttons'
    ),
    dcc.Graph(id='the_graph'),
   
])


@app.callback(
    Output(component_id='the_graph', component_property='figure'), 
    [Input('radio-buttons', 'value')]
)

def update_figure(category):  

    categories = ([
        {'title':'2018 World Happiness Score', 'color': 'blues', 'data':'Happiness score'},
        {'title': '2018 GDP per capita', 'color': 'icefire', 'data':'Log GDP per capita'},
        {'title':'2018 World Happiness Score', 'color': 'blues', 'data':'Happiness score'},
        {'title': '2018 GDP per capita', 'color': 'icefire', 'data':'Log GDP per capita'},
        {'title':'2018 World Happiness Score', 'color': 'blues', 'data':'Happiness score'},
    
    ])
    fig = go.Figure(data=go.Choropleth(
        locations = df['CODE'],
        text = df['Country'],
        colorscale = categories[category]['color'],
        autocolorscale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        z = df[categories[category]['data']],
        reversescale=True,
        colorbar_title = categories[category]['title'],
        ))

    fig.update_layout(
        title_text=categories[category]['title'],
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
    )
    return fig



app.run_server(debug=True, dev_tools_hot_reload=True, use_reloader=False,)