#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash import Dash
from dash.dependencies import Input, Output
import dash_daq as daq
from sklearn.linear_model import LogisticRegression
import plotly.graph_objs as go

app = Dash(__name__)
server = app.server
app.title='Reddit User Submission Dashboard'

# dash apps are unstyled by default
# this css I'm using was created by the author of Dash
# and is the most commonly used style sheet
app.css.append_css({
                   "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
                   })

# Logistic model2: cop, black, man, teen
train_pca_other_df = pd.read_csv("/data/train_pca_other_df06032019.csv")
test_pca_other_df = pd.read_csv("/data/test_pca_other_df06032019.csv")

m=LogisticRegression(solver = 'lbfgs')
m.fit(train_pca_other_df[['cop', 'black', 'man', 'teen']],train_pca_other_df.is_russian)

def preds(cop, black, man, teen):
    model = m
    df = pd.DataFrame([[cop, black, man, teen]], columns = ['cop', 'black', 'man', 'teen'])
    predict_prob = model.predict_proba(df).tolist()
    print(predict_prob)
    predict_prob = predict_prob[0][1]
    if predict_prob > 0.99:
        prediction = 'Yes'
    else:
        prediction = 'No'
    return prediction


# Logistic model3: russian_prop, black man, chicago cop, kill unarmed
m2=LogisticRegression(solver = 'lbfgs')
m2.fit(train_pca_other_df[['russian_prop','black man', 'chicago cop', 'kill unarmed']],train_pca_other_df.is_russian)

def preds2(russianProp, blackMan, chicagoCop, killUnarmed):
    model = m2
    df = pd.DataFrame([[russianProp, blackMan, chicagoCop, killUnarmed]], columns = ['russian_prop','black man', 'chicago cop', 'kill unarmed'])
    predict_prob = model.predict_proba(df).tolist()
    print(predict_prob)
    predict_prob = predict_prob[0][1]
    if predict_prob > 0.5:
        prediction = 'Yes'
    else:
        prediction = 'No'
    return prediction

#scatter plot
scatter_sub = pd.read_csv("/data/submissions_plot_06032019.csv")
scatter_sub['y'] = scatter_sub['y'].astype(str)

app.layout = html.Div([
                       
                       dcc.Graph(
                                 id = 'scatter_chart',
                                 figure={
                                 'data': [
                                          go.Scatter(
                                                     x=scatter_sub[scatter_sub['y'] == i]['Dimension1'],
                                                     y=scatter_sub[scatter_sub['y'] == i]['Dimension2'],
                                                     text=scatter_sub[scatter_sub['y'] == i]['SubmissionTitle'],
                                                     mode='markers',
                                                     opacity=0.8,
                                                     marker={
                                                     'size': 4,
                                                     'line': {'width': 0.5, 'color': 'white'}
                                                     },
                                                     name=i
                                                     ) for i in scatter_sub.y.unique()
                                          ],
                                 'layout': go.Layout(
                                                     xaxis={'title': 'Dimension 1'},
                                                     yaxis={'title': 'Dimension 2'},
                                                     margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                                                     legend={'x': 0, 'y': 1},
                                                     hovermode='closest'
                                                     )
                                 }
                                 ),
                       html.Br(), html.Br(),
                       html.H4('Logistic Regression Model: Option 1'),
                       html.H5(id='output-prediction', style={'color':'blue','fontSize': 15}),
                       
                       html.H5('cop, tf-idf score', style={'fontSize': 15}),
                       html.Br(), html.Br(),
                       daq.Slider(
                                  id='input-cop',
                                  min=0,
                                  max=5,
                                  step=.1,
                                  dots=False,
                                  handleLabel={"showCurrentValue": True,"label": "Value"},
                                  value=0.5),
                       
                       html.H5('black,tf-idf score', style={'fontSize': 15}),
                       html.Br(), html.Br(),
                       daq.Slider(
                                  id='input-black',
                                  min=0,
                                  max=5,
                                  dots=False,
                                  handleLabel={"showCurrentValue": True,"label": "Value"},
                                  step=.1,
                                  value=0.5),
                       
                       html.H5('man, tf-idf score', style={'fontSize': 15}),
                       html.Br(), html.Br(),
                       daq.Slider(
                                  id='input-man',
                                  min=0,
                                  max=5,
                                  dots=False,
                                  handleLabel={"showCurrentValue": True,"label": "Value"},
                                  step=.1,
                                  value=0.5),
                       html.H5('teen, tf-idf score', style={'fontSize': 15}),
                       html.Br(), html.Br(),
                       daq.Slider(
                                  id='input-teen',
                                  min=0,
                                  max=5,
                                  dots=False,
                                  handleLabel={"showCurrentValue": True,"label": "Value"},
                                  step=.1,
                                  value=0.5),
                       
                       html.Br(), html.Br(),
                       html.H4('Logistic Regression Model: Option 2'),
                       html.H5(id='output-prediction2', style={'color':'blue','fontSize': 15}),
                       
                       daq.ToggleSwitch(
                                        id='input-russianProp',
                                        label='URL link to Russian Propoganda (toggle default is false)',
                                        value=False),
                       
                       html.H5('black man, tf-idf score', style={'fontSize': 15}),
                       html.Br(), html.Br(),
                       daq.Slider(
                                  id='input-blackMan',
                                  min=0,
                                  max=5,
                                  dots=False,
                                  handleLabel={"showCurrentValue": True,"label": "Value"},
                                  step=.1,
                                  value=0.5),
                       html.H5('chicago cop, tf-idf score', style={'fontSize': 15}),
                       html.Br(), html.Br(),
                       daq.Slider(
                                  id='input-chicagoCop',
                                  min=0,
                                  max=5,
                                  dots=False,
                                  handleLabel={"showCurrentValue": True,"label": "Value"},
                                  step=.1,
                                  value=0.5),
                       html.H5('kill unarmed, tf-idf score', style={'fontSize': 15}),
                       html.Br(), html.Br(),
                       daq.Slider(
                                  id='input-killUnarmed',
                                  min=0,
                                  max=5,
                                  dots=False,
                                  handleLabel={"showCurrentValue": True,"label": "Value"},
                                  step=.1,
                                  value=0.5),
                       html.Br(), html.Br(),
                       ])

# insert callbacks
@app.callback(
              dash.dependencies.Output('output-prediction', 'children'),
              [
               dash.dependencies.Input('input-cop', 'value'),
               dash.dependencies.Input('input-black', 'value'),
               dash.dependencies.Input('input-man', 'value'),
               dash.dependencies.Input('input-teen', 'value')])
def callback_pred(cop, black, man, teen):
    # pass values from the function on to our prediction function
    # defined in setup
    pred = preds(cop = cop,
                 black = black,
                 man = man,
                 teen = teen)
                 # return a string that will be rendered in the UI
    return "Is submission title predicted to have come from a Russian account: {}".format(pred)

@app.callback(
              dash.dependencies.Output('output-prediction2', 'children'),
              [
               dash.dependencies.Input('input-russianProp', 'value'),
               dash.dependencies.Input('input-blackMan', 'value'),
               dash.dependencies.Input('input-chicagoCop', 'value'),
               dash.dependencies.Input('input-killUnarmed', 'value')])
def callback_pred2(russianProp, blackMan, chicagoCop, killUnarmed):
    # pass values from the function on to our prediction function
    # defined in setup
    pred = preds2(russianProp,
                  blackMan,
                  chicagoCop,
                  killUnarmed)
                 # return a string that will be rendered in the UI
    return "Is submission title predicted to have come from a Russian account: {}".format(pred)



if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True, port=8050)
