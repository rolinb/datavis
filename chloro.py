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
    if category == 0 :
        fig = go.Figure(data=go.Choropleth(
        locations = df['CODE'],
        text = df['Country'],
        colorscale = 'blues',
        autocolorscale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        z = df['Happiness score'],
        reversescale=True,
        colorbar_title = 'Happiness Score',
        ))

        fig.update_layout(
            title_text='2018 Happiness Scores',
            geo=dict(
                showframe=False,
                showcoastlines=False,
                projection_type='equirectangular'
            ),
            
        )
    elif category == 1:
        fig = go.Figure(data=go.Choropleth(
        locations = df['CODE'],
        text = df['Country'],
        colorscale = 'edge',
        autocolorscale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        z = df['Log GDP per capita'],
        reversescale=True,
        colorbar_title = 'Log GDP',
        ))

        fig.update_layout(
            title_text='2018 Log GDP per capita',
            geo=dict(
                showframe=False,
                showcoastlines=False,
                projection_type='equirectangular'
            ),
            
        )

    elif category == 2:
        fig = go.Figure(data=go.Choropleth(
        locations = df['CODE'],
        text = df['Country'],
        colorscale = 'edge',
        autocolorscale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        z = df['Freedom to make life choices'],
        reversescale=True,
        colorbar_title = 'Freedom to make life choices',
        ))

        fig.update_layout(
            title_text='2018 Freedom to make life choices',
            geo=dict(
                showframe=False,
                showcoastlines=False,
                projection_type='equirectangular'
            ),
            
        )

    elif category == 3:
        fig = go.Figure(data=go.Choropleth(
        locations = df['CODE'],
        text = df['Country'],
        colorscale = 'icefire',
        autocolorscale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        z = df['Generosity'],
        reversescale=True,
        colorbar_title = 'Generosity',
        ))

        fig.update_layout(
            title_text='2018 Generosity',
            geo=dict(
                showframe=False,
                showcoastlines=False,
                projection_type='equirectangular'
            ),
            
        )

    elif category == 4:
        fig = go.Figure(data=go.Choropleth(
        locations = df['CODE'],
        text = df['Country'],
        colorscale = 'edge',
        autocolorscale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        z = df['Social support'],
        reversescale=True,
        colorbar_title = 'Social Support',
        ))

        fig.update_layout(
            title_text='2018 Social Support',
            geo=dict(
                showframe=False,
                showcoastlines=False,
                projection_type='equirectangular'
            ),
            
        )
    return fig


app.run_server(debug=True, dev_tools_hot_reload=True, use_reloader=False,)