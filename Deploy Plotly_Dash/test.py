import seaborn as sns
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

df = sns.load_dataset('taxis')
df.dropna(inplace=True)
df.reset_index(inplace=True)
df['day'] = df['pickup'].dt.day
df['month'] = df['pickup'].dt.month
df['year'] = df['pickup'].dt.year
df

def sunburst_chart():
    fig = px.sunburst(df_new, path=['payment', 'color'], values='total')
    return fig

def bar_chart():
    bar_data = df_new.groupby(['pickup_borough'])['total'].sum().reset_index()

    fig = px.bar(bar_data, x="pickup_borough", y="total", title='Total number of ') 
    return fig

def line_chart():
    line_data = df_new.groupby(['pickup_borough','day'])['total'].sum().reset_index()

    fig = px.line(line_data, x='day', y='total', color='pickup_borough', markers=True)
    return fig
    

app = dash.Dash(__name__)
app.layout = html.Div(children=[html.H1('Flight Delay Time Statistics',
                                        style={'textAlign': 'center', 'color': '#503D36', 'font-size': 30}),
                                
                                dcc.Dropdown([2, 3], value=3, id='input-month'),

                                html.Br(),
                                html.Br(), 
                                
                                # Output component - Segment 2
                                html.Div([html.Div(dcc.Graph(id='sunburst-plot')),
                                          html.Div(dcc.Graph(id='bar-plot'))],
                                         style={'display': 'flex'}),
                                
                                # Output component - Segment 3                                       
                                html.Div(dcc.Graph(id='line-plot'), style={'width':'100%'}),
                               ])

@app.callback( [Output(component_id='sunburst-plot', component_property='figure'),
               Output(component_id='bar-plot', component_property='figure'),
               Output(component_id='line-plot', component_property='figure')],
               Input(component_id='input-month', component_property='value'))

def get_graph(entered_month):
    global df_new
    df_new =  df[df['month']==int(entered_month)]

    fig1 = sunburst_chart()
    fig2 = bar_chart()
    fig3 = line_chart()  

    
    return [fig1, fig2, fig3]

# Run the app
if __name__ == '__main__':
    app.run_server()