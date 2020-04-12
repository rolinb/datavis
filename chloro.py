import plotly.graph_objects as go
import pandas as pd

bars = ['Happiness score', 'Dystopia (1.88) + residual', 'Explained by: GDP per capita',
    'Explained by: Social support',	'Explained by: Healthy life expectancy', 
    'Explained by: Freedom to make life choices',	'Explained by: Generosity',
    'Explained by: Perceptions of corruption']

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
app.logger.info(df)

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
        options=[
            #This order needs to match the arrays below 
            {'label': 'Happiness Rank', 'value':0},
            {'label': 'Log GDP per capita', 'value':1},
            {'label': 'Social Support', 'value':2},
            {'label': 'Life Expectancy', 'value':3},
            {'label': 'Generosity', 'value':4},
            {'label': 'Perception of Corruption', 'value':5},
            {'label': 'Freedom', 'value':6},
            {'label': 'Dystopia (1.88) + residual', 'value':7},
        ],
        value=0,
        id='radio-buttons-left'
        ),
        dcc.Graph(id='the_graph_left'),
    ], className="left", style={'width': '49%', 'display': 'inline-block'}),
    html.Div([
        dcc.Dropdown(
        options=[
            {'label': 'Happiness Rank', 'value':0},
            {'label': 'Log GDP per capita', 'value':1},
            {'label': 'Social Support', 'value':2},
            {'label': 'Life Expectancy', 'value':3},
            {'label': 'Generosity', 'value':4},
            {'label': 'Perception of Corruption', 'value':5},
            {'label': 'Freedom', 'value':6},
            {'label': 'Dystopia (1.88) + residual', 'value':7},
        ],
        value=0,
        id='radio-buttons'
        ),
        dcc.Graph(id='the_graph'),
    ],className="right", style={'width': '49%', 'display': 'inline-block'}),
    #start bar charts for countries
    html.Div([
        dcc.Dropdown(
        options=[{'label': i, 'value': i} for i in df.Country],
        value=['Canada'],
        id='country-selector',
        multi=True,
        style={'width': '49%', 'display': 'inline-block'}),
        dcc.Dropdown(
        options=[{'label': i, 'value': i} for i in bars],
        value=['Happiness score'],
        id='bars-selector',
        multi=True,
        style={'width': '49%', 'display': 'inline-block'}),
        dcc.Graph(id='country-graph'),
    ]) 
])


@app.callback(
    Output(component_id='the_graph', component_property='figure'), 
    [Input('radio-buttons', 'value')]
)

def update_figure(category):  
    #this array is what needs to match

    categories = ([
        {'title':'2018 World Happiness Score', 'color': 'blues_r', 'data':'Happiness score'},
        {'title': '2018 Log GDP per capita', 'color': 'greens', 'data':'Log GDP per capita'},
        {'title':'2018 Social Support', 'color': 'purples', 'data':'Social support'},
        {'title': '2018 Life Expectancy', 'color': 'oranges', 'data':'Healthy life expectancy at birth'},
        {'title':'2018 Generosity', 'color': 'blues', 'data':'Generosity'},
        {'title':'2018 Perception of Corruption', 'color': 'reds', 'data':'Perceptions of corruption'},
        {'title':'2018 Freedom', 'color': 'pinkyl', 'data':'Freedom to make life choices'},
        {'title':'2018 Dystopia', 'color': 'greys', 'data':'Dystopia (1.88) + residual'},
    
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
    app.logger.info("in update")
    fig.update_layout(
        title_text=categories[category]['title'],
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
    )
    return fig


@app.callback(
    Output(component_id='the_graph_left', component_property='figure'), 
    [Input('radio-buttons-left', 'value')]
)

def update_figure(category):  

    categories = ([
        {'title':'2018 World Happiness Score', 'color': 'blues_r', 'data':'Happiness score'},
        {'title': '2018 Log GDP per capita', 'color': 'greens', 'data':'Log GDP per capita'},
        {'title':'2018 Social Support', 'color': 'purples', 'data':'Social support'},
        {'title': '2018 Life Expectancy', 'color': 'oranges', 'data':'Healthy life expectancy at birth'},
        {'title':'2018 Generosity', 'color': 'blues', 'data':'Generosity'},
        {'title':'2018 Perception of Corruption', 'color': 'reds', 'data':'Perceptions of corruption'},
        {'title':'2018 Freedom', 'color': 'pinkyl', 'data':'Freedom to make life choices'},
        {'title':'2018 Dystopia', 'color': 'greys', 'data':'Dystopia (1.88) + residual'},
    
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

#this is for the country graph
@app.callback(
    Output(component_id='country-graph', component_property='figure'), 
    [Input('country-selector', 'value'), Input('bars-selector', 'value')]
)

def update_figure(countries, bars):  
    countries.sort()


    colors = {
    'Happiness score' : 'rgb(237, 239, 93)', 
    'Dystopia (1.88) + residual': 'rgb(37, 37, 37)' , 
    'Explained by: GDP per capita': 'rgb(0, 68, 27)',
    'Explained by: Social support': 'rgb(63, 0, 125)',	
    'Explained by: Healthy life expectancy': 'rgb(127,39,4)', 
    'Explained by: Freedom to make life choices': 'rgb(241, 109, 122)',	
    'Explained by: Generosity': 'rgb(8,81,156)',
    'Explained by: Perceptions of corruption' : 'rgb(165, 15, 21)'
    }

    
    fig = go.Figure(data=[         
    ])
    for bar in bars:
        fig.add_bar(name=bar, x=countries, y=df.loc[df['Country'].isin(countries)][bar], marker_color=colors[bar]),
    # Change the bar mode
    fig.update_layout(barmode='group')


    return fig


app.run_server(debug=True, dev_tools_hot_reload=True, dev_tools_hot_reload_interval=500,)