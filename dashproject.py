import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import csv

console = pd.read_csv("console.csv",index_col=0)
console.reset_index(inplace=True)
steam = pd.read_csv("steamplayers.csv",index_col=0)
steam.reset_index(inplace=True)
anpre = pd.read_csv("androidpremium.csv",index_col=0)
sterev = pd.read_csv("steamrevenue.csv",index_col=0)
freean = pd.read_csv("freemiumandroid.csv",index_col=0)
freeap = pd.read_csv("freemiumapple.csv",index_col=0)

app = dash.Dash()

app.layout = html.Div(
    children=[
        html.H1('Video Game Industry'),
        html.Div(children='''
        Created by: Wiko Leonardo
    '''),
    dcc.Tabs([
        dcc.Tab(label='Console', children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': console['index'], 'y': console['Units'],
                            'type': 'bar', 'name': 'console'},
                        {'x': console['index'], 'y': console['GTAV'],
                            'type': 'bar', 'name': 'GTAV'},
                        {'x': console['index'], 'y': console['Mario Kart'],
                            'type': 'bar', 'name': 'Mario Kart'},
                    ],
                    'layout' : {
                    'title':'Console Sales (in Millions)'}
                }
            ),html.Div([
                                    html.P("Data gathered by using VGChartz")]),
        ]),
        dcc.Tab(label='PC', children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': steam['MONTH'], 'y': steam['PEAK'],
                            'type': 'line', 'name': 'steam'},
                    ],
                    'layout' : {
                    'title':'Steam Peak Concurrent Players'}
                }
            ),
                dcc.Graph(
                figure={
                    'data': [
                        {'x': sterev['index'], 'y': sterev['PeakPlayers'],
                            'type': 'bar', 'name': 'PeakPlayers'},
                            {'x': sterev['index'], 'y': sterev['AvgConcurrent'],
                            'type': 'bar', 'name': 'AvgConcurrent'},
                    ],
                    'layout' : {
                    'title':'Steam Game Categories Peak Players'}
                }
            ),html.Div([
                                    html.P("Data gathered by using steamdb and steamcharts")])
        ]),
        dcc.Tab(label='Mobile', children=[
                                            html.Div([
                                    html.P('Freemium'),
                                    dcc.Dropdown(value='',
                                                 id='filter-freemium',
                                                 options=[{'label': 'Android','value': 'Android'}, 
                                                 {'label': 'Apple','value': 'Apple'},
                                                 {'label': 'None','value': ''}])
                                ],
                                         className='col-3'),
                                         html.Div(id='freemium'),
                                         html.Div([
                                    html.P("Data gathered by using Sensor Tower")]),

                                         dcc.Graph(
                figure={
                    'data': [
                        {'x': anpre['Name'], 'y': anpre['downloads(in thousands)'],
                            'type': 'bar', 'name': 'Downloads'},

                        {'x': anpre['Name'], 'y': anpre['earnings(in thousands)'],
                         'type': 'bar', 'name': 'Earnings'},
                    ],
                    'layout' : {
                    'title':'Top 10 Android Premium Apps in US (in thousands)'}
                }
            ),html.Div([
                                    html.P("No apple freemium chart because I can't get the data")])
        ]),
    ])
    ])

@app.callback(
    Output(component_id = 'freemium', component_property = 'children'),
    [Input(component_id='filter-freemium', component_property = 'value')],

)

def freemium(tes):
    if tes == 'Android':
        return dcc.Graph(
            id = 'Android',
                figure = {
                    'data':[
                        {'x':freean['Name'],'y':freean['revenue(million)'], 'type':'bar','name':tes}
                    ],
                    'layout' : {
                        'title':'Top 10 Freemium Android Apps Revenue in the US (in millions)'
                            }           
                        }
                )
    elif tes == 'Apple':
        return dcc.Graph(
            id = 'Apple',
                figure = {
                    'data':[
                        {'x':freeap['Name'],'y':freeap['revenue(million)'], 'type':'bar','name':tes}
                    ],
                    'layout' : {
                        'title':'Top 10 Freemium Apple Apps Revenue in the US (in millions)'
                            }           
                        }
                )

# @app.callback(
#     Output(component_id = 'two', component_property = 'children'),
#     [Input(component_id='test', component_property = 'value')],

# )

# def aga(zes):
#     return "Input: {}".format(zes)

if __name__ == '__main__':
    app.run_server(debug=True)