import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import os

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#F0F8FF',
    'text': '#00008B'
}
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("FullPolarity1.csv")

fig = go.Figure()

fig.add_trace(
    go.Scatter(x=list(df.Date), y=list(df.Sentiment), line_color='#ff7f0e'))

print(df.index)

fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"

    )
)

fig.update_layout(title_text="User Political Polarization over time")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

repubfig = go.Figure()

repubfig.add_trace(
    go.Scatter(x=list(df.Date), y=list(df.RepubSentiment), line_color='#d62728'))

repubfig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"

    )
)

repubfig.update_layout(title_text="Republican Political Polarization over Time")

repubfig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

demfig = go.Figure()

demfig.add_trace(
    go.Scatter(x=list(df.Date), y=list(df.DemSentiment), line_color='#17becf'))

demfig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"

    )
)

demfig.update_layout(title_text="Democrat Political Polarization over Time")

demfig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

markdown_text = '''
### Political Polarization on Twitter over Time
Creator: Jay Vogel, [Github](https://github.com/Lavarider)

This is an interactive dashboard modeling polarization over time on Twitter.

Higher means there is more polarization, and is worse, while negative implies less polarization, and is better.

This was calculated using a database of 16 million tweets and Natural Language Processing, and the full background code is available on Github.

It automatically updates every day, and you can look at Democratic Polarization, Republican Polarization, or General Polarization!
'''


app.layout = html.Div([
    dcc.Markdown(children=markdown_text,
        style={
            'backgroundColor': colors['background'],
            'textAlign': 'center',
            'color': colors['text']
        }),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    dcc.Graph(
        id='repubgraph',
        figure=repubfig
    ),

    dcc.Graph(
        id='demgraph',
        figure=demfig
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)
