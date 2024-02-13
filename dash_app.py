import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

app = dash.Dash(__name__)

text1 = '''The gender had been identified via the specific gender words that the commenters used.\n
        From all 3 video, it shows that the majority of commenters is male. Eventhough there are commmenter accounts 
        that cannot be defined their gender,
        this information might be useful to support the idea that
         male is more interested about the EV Car than female.'''
vdo1_text1 = '''By categorized comments' opinion using keyword, the majority of the commenters' opinion is negative (76.13%) followed by Neutral/Irrelavent (15.06%), 
        positive (7.95%), and questionable (0.81%), respectively.'''
vdo1_text2 = '''From the chart above, the result shows that majority of male opinion is negative, whereas the majority of female opinion is positive.
        This inconsistent opinion is a good point to further explore in the field of marketing. Only this result cannot be concluded about the opinion of
        male and female toward EV car in Thailand. Because there are the comments that cannot be defined of commenter's gender. In addition, 
        the percentage is calculated based on the like that each commenter got which the account that clicked like can be either of gender.'''

vdo2_text1 = '''By categorized comments' opinion using keyword, the majority of the commenters' opinion is neutral/irrelavent 35.90% (28 commenters) 
        followed by questionable 32.05% (25 commenters), negative 17.95% (14 commenters), and positive 14.10%(11 commenters), respectively.'''

vdo2_text2 = '''From the chart above, it demonstrates the percent of comment type in each gender. 
        The result shows that 50% of female has positive opinion and another half has neutral/irrelavent opinion toward EV car.
        While 40.74% of male has questionable opinion, follow by neutral/irrelavent (27.78%), negative (16.67%), and positive (14.81%) opinion, respectively.
        The commenter account that cannot be defined its gender, the majority of opinion is neutral/irrelavent (54.55%), follow by negative (22.73%), 
        questionable (13.64%), and positive (9.09%) opinion.'''

vdo3_text1 = '''By categorized comments' opinion using keyword, the majority of the commenters' opinion is neutral/irrelavent at 46.92% (38 commenters)
        followed by questionable 24.69% (20 commenters) , negative 22.22% (18 commenters), and positive 6.17%(5 commenters), respectively.'''

vdo3_text2 = '''From the chart above, it demonstrates the percent of comment type in each gender. 
        The result shows that 66.67% (2 commenters) of female has neutral/irrelavent opinion, and 33.33% (1 commenter) has negative opinion toward EV car.
        While 39.58% of male has neutral/irrelavent opinion, follow by questionable (33.33%), negative (22.92%), and positive (4.17%) opinion, respectively.
        The commenter account that cannot be defined its gender, the majority of opinion is neutral/irrelavent (56.67%), follow by negative (20.00%), 
        questionable (13.33% ), and positive (10%) opinion.'''

text_sum = '''From the comments of all 3 videos, the result seems inclusive and researh further is needed. However, since the video 3 have low amount of commenters.
        If the result of video 3 is not considered, the result shows that female tends to have positive opinion toward EV Car. While male tends to have negative and questionable opinion.'''

#chart1 
#comment number >> axis y is account 

x = ['Video 1 ','Video 2','Video 3']
y = [610,78,82]

height = 200 * 2
wid = 500
# Use textposition='auto' for direct text
fig1 = go.Figure(data=[go.Bar(
            x=x, y=y,
            text=y,
            textposition='auto',
        )])
fig1.update_layout(
    showlegend=False,
    #title_text="Comment Numbers",
    #title_x=0.5,
    height=height,
    #width=wid,
    #xaxis_title="",
    yaxis_title="Account Number"
)
#fig1.show()

# chart2
video = ['Video 1', 'Video 2', 'Video 3']

fig2 = go.Figure(data=[
    go.Bar(name='Female', x=video, y=[35, 2, 3], text=[35, 2, 3], textposition='outside'),
    go.Bar(name='Male', x=video, y=[230, 54, 49], text=[230, 54, 49], textposition='outside'),
    go.Bar(name='Cannot Define', x=video, y=[345, 22, 30], text=[345, 22, 30], textposition='outside')
])
# Change the bar mode
fig2.update_layout(barmode='group', yaxis_title="Account Number", legend_title="Gender", height=550)
#fig2.show()

# vdo1bar
gender=['Female', 'Male', 'Cannot Define']

vdo1bar = go.Figure(data=[
    go.Bar(name='Negative', x=gender, y=[1.621622, 84.590861, 57.857143], text='', textposition='outside', marker={'color': ['#EF553B', '#EF553B', '#EF553B']}),
    go.Bar(name='Positive', x=gender, y=[77.837838, 5.791711, 3.061224], text='', textposition='outside', marker={'color': ['#00CC96', '#00CC96', '#00CC96']}),
    go.Bar(name='Questionable', x=gender, y=[2.702703, 0.478215, 1.734694], text='', textposition='outside', marker={'color': ['#929AFC', '#929AFC', '#929AFC']}),
    go.Bar(name='Neutral/Irrelavent', x=gender, y=[17.837838, 9.139214, 37.346939], text='', textposition='outside', marker={'color': ['gray', 'gray', 'gray']})])

# Change the bar mode
vdo1bar.update_layout(
    barmode='group', yaxis_title="%", 
    title={
        'text':"%weight of opinion by gender",
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    legend=dict(x=0.1, y=-0.1, traceorder="normal", orientation="h"), 
    width=None,height=None)
#vdo1bar.show()

# vdo2bar
gender=['Female', 'Male', 'Cannot Define']

vdo2bar = go.Figure(data=[
    go.Bar(name='Negative', x=gender, y=[0.0, 16.66667, 22.727273], text='', textposition='outside', marker={'color': ['#EF553B', '#EF553B', '#EF553B']}),
    go.Bar(name='Positive', x=gender, y=[50.0, 14.814815, 9.090909], text='', textposition='outside', marker={'color': ['#00CC96', '#00CC96', '#00CC96']}),
    go.Bar(name='Questionable', x=gender, y=[0.0, 40.740741, 13.636364], text='', textposition='outside', marker={'color': ['#929AFC', '#929AFC', '#929AFC']}),
    go.Bar(name='Neutral/Irrelavent', x=gender, y=[50.0, 27.777778, 54.545455], text='', textposition='outside', marker={'color': ['gray', 'gray', 'gray']})])

# Change the bar mode
vdo2bar.update_layout(
    barmode='group', yaxis_title="%", 
    title={
        'text':"%weight of opinion by gender",
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    legend=dict(x=0.1, y=-0.1, traceorder="normal", orientation="h"), 
    width=None,height=None)
#vdo2bar.show()

# vdo3bar
gender=['Female', 'Male', 'Cannot Define']

vdo3bar = go.Figure(data=[
    go.Bar(name='Negative', x=gender, y=[33.333333, 22.916667, 20.0], text='', textposition='outside', marker={'color': ['#EF553B', '#EF553B', '#EF553B']}),
    go.Bar(name='Positive', x=gender, y=[0.0, 4.166667, 10.0], text='', textposition='outside', marker={'color': ['#00CC96', '#00CC96', '#00CC96']}),
    go.Bar(name='Questionable', x=gender, y=[0.0, 33.333333, 13.333333], text='', textposition='outside', marker={'color': ['#929AFC', '#929AFC', '#929AFC']}),
    go.Bar(name='Neutral/Irrelavent', x=gender, y=[66.666667, 39.583333, 56.666667], text='', textposition='outside', marker={'color': ['gray', 'gray', 'gray']})])

# Change the bar mode
vdo3bar.update_layout(
    barmode='group', yaxis_title="%", 
    title={
        'text':"%weight of opinion by gender",
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    legend=dict(x=0.1, y=-0.1, traceorder="normal", orientation="h"), 
    width=None,height=None)
#vdo3bar.show()

#Plot Sunburst
#sun1
##create new dataframe from df_opinion_gender
gender = ["Cannot Define", "Cannot Define", "Cannot Define","Cannot Define", "Female", "Female","Female","Female","Male", "Male","Male", "Male"]
opinion = ["Negative", "Positive", "Questionable", "Neutral/Irrelavent", "Negative", "Positive", "Questionable", "Neutral/Irrelavent","Negative", "Positive", "Questionable", "Neutral/Irrelavent",]
percent = [11.498682, 0.608396, 0.344758, 7.422430, 0.06840, 2.920300, 0.101399, 0.669235, 64.571081, 4.421010, 0.365038, 6.976273]
df_new = pd.DataFrame(
    dict(gender=gender, opinion=opinion, percent=percent))
sun1 = px.sunburst(
    df_new, path=['opinion', 'gender'], values='percent', title ='Opinion of Commenters',color='opinion',
    color_discrete_map={'Negative':'#EF553B', 'Positive':'#00CC96', 'Questionable':'##929AFC',"Neutral/Irrelavent":'gray',})
sun1.update_layout(title={'text':"Opinion of Commenters",
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'})
#sun1.show()

#sun2
#create new dataframe from df_gb_gen
gender = ["Cannot Define", "Cannot Define", "Cannot Define","Cannot Define", "Female", "Female","Female","Female","Male", "Male","Male", "Male"]
opinion = ["Negative", "Positive", "Questionable", "Neutral/Irrelavent", "Negative", "Positive", "Questionable", "Neutral/Irrelavent","Negative", "Positive", "Questionable", "Neutral/Irrelavent",]
percent = [6.410256, 2.564103, 3.846154, 15.384615, 0.0, 1.282051, 0.0, 1.282051, 11.538462, 10.256410, 28.205128, 19.230769]
df_new = pd.DataFrame(
    dict(gender=gender, opinion=opinion, percent=percent))
sun2 = px.sunburst(
    df_new, path=['opinion', 'gender'], values='percent', title ='Opinion of Commenters',color='opinion',
    color_discrete_map={'Negative':'#EF553B', 'Positive':'#00CC96', 'Questionable':'##929AFC',"Neutral/Irrelavent":'gray',})
sun2.update_layout(title={'text':"Opinion of Commenters",
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'})
#sun2.show()

#sun3
#create new dataframe from df_gb_gen2
gender = ["Cannot Define", "Cannot Define", "Cannot Define","Cannot Define", "Female", "Female","Female","Female","Male", "Male","Male", "Male"]
opinion = ["Negative", "Positive", "Questionable", "Neutral/Irrelavent", "Negative", "Positive", "Questionable", "Neutral/Irrelavent","Negative", "Positive", "Questionable", "Neutral/Irrelavent",]
percent = [7.407407, 3.703704, 4.938272, 20.987654, 1.234568, 0.0, 0.0, 2.469136, 13.580247, 2.469136, 19.753086, 23.46790]
df_new = pd.DataFrame(
    dict(gender=gender, opinion=opinion, percent=percent))
sun3 = px.sunburst(
    df_new, path=['opinion', 'gender'], values='percent', title ='Opinion of Commenters',color='opinion',
    color_discrete_map={'Negative':'#EF553B', 'Positive':'#00CC96', 'Questionable':'##929AFC',"Neutral/Irrelavent":'gray',})
sun3.update_layout(title={'text':"Opinion of Commenters",
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'})
#sun3.show()

# Create app layout
app.layout = html.Div(
    [
        dcc.Store(id="aggregate_data"),
        # empty Div to trigger javascript file for graph resizing
        html.Div(id="output-clientside"),
        html.Div(
            [   
                html.Div(
                    [
                        html.Div(
                            [
                                #html.H4(style={"margin-bottom": "50px"}),
                                html.H4(
                                    "What do Thai people think about EV car?",
                                    style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center',"font-weight": "bold"},
                                ),
                                html.H5(
                                    "Analysis and interpretation of Thai people opinions via comments in Tiktok & Youtube video about EV car",
                                    style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center',"margin-top": "0px"},
                                ),
                            ]
                        )
                    ],
                    className="three column",
                    id="title",
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        dbc.Row([
                            #dbc.Col([ #for left space from margin
                            #]),
                            dbc.Col([
                                html.H6(
                                    "Source Videos",
                                    style={
                                        "margin-top": "0",
                                        "font-weight": "bold",
                                        "text-align": "left",
                                    },
                                ),
                                dbc.Row([
                                    dbc.Col([
                                    html.Iframe(src='https://www.youtube.com/embed/bELcB1K1Fqg',
                                                width='100%',
                                                height='315')
                                    ]),
                                    html.P("Video 1",
                                            style={
                                                "margin-top": "0",
                                                "font-weight": "bold",
                                                "text-align": "center",
                                            },
                                    ),
                                    dbc.Col([
                                        dcc.Link(
                                            children='TikTok: My take on EV car purchase.',
                                            href='https://www.tiktok.com/@ckfastwork/video/7166548702008511771?q=my%20take%20on&t=1672803382660', className='someClass',
                                        ),
                                        html.P("Publisher: ckfastwork"),
                                        html.P("Published Date: 16-Nov-2022"),
                                        html.P("Likes: 105.7K"),
                                        html.P("Views: 1.8M"),
                                    ]),
                                ]),
                                dbc.Row([
                                    dbc.Col([
                                    html.Iframe(src='https://www.youtube.com/embed/Fncg9oH16O0',
                                                width='100%',
                                                height='315')
                                    ]),
                                    html.P("Video 2",
                                            style={
                                                "margin-top": "0",
                                                "font-weight": "bold",
                                                "text-align": "center",
                                            },
                                    ),
                                    dbc.Col([
                                        dcc.Link(
                                            children='Youtube: คุยเรื่องรถไฟฟ้า Feat. นพ Extreme IT l #แพนกันวันพุธ',
                                            href='https://www.youtube.com/watch?v=Fncg9oH16O0', className='someClass',
                                        ),
                                        html.P("Publisher: beartai แบไต๋"),
                                        html.P("Published Date: 28-Sep-2022"),
                                        html.P("Likes: 312K"),
                                        html.P("Views: 1.3K"),
                                    ]),
                                ]),
                                dbc.Row([
                                    dbc.Col([
                                    html.Iframe(src='https://www.youtube.com/embed/K_CNEJ_M97w',
                                                width='100%',
                                                height='315')
                                    ]),
                                    html.P("Video 3",
                                            style={
                                                "margin-top": "0",
                                                "font-weight": "bold",
                                                "text-align": "center",
                                            },
                                    ),
                                    dbc.Col([
                                        dcc.Link(
                                            children='Youtube: อย่าเพิ่งซื้อรถยนต์ไฟฟ้า ถ้าคุณยังไม่รู้เรื่องนี้ !',
                                            href='https://www.youtube.com/watch?v=K_CNEJ_M97w', className='someClass',
                                        ),
                                        html.P("Publisher: beartai แบไต๋"),
                                        html.P("Published Date: 08-Aug-2021"),
                                        html.P("Likes: 21K"),
                                        html.P("Views: 1.6M"),
                                    ]),
                                ]),
                            ]),
                        ]),
                    ],
                    className="pretty_container_two_columns",
                    id="part_one",
                    style={"text-align": "justify"},
                ),
                html.Div(
                    [
                        html.Div(
                            style={
                                "display": "flex",
                                "justify-content": "center",
                                "align-items": "center"
                            },
                        ),
                        html.Div(
                            [
                                html.Div(
                                    style={
                                        "display": "flex",
                                        "justify-content": "center",
                                        "align-items": "center"
                                    },
                                    children=[
                                        html.H6(            
                                            "Commenter Number",
                                            style={                
                                                "margin-top": "20",                
                                                "font-weight": "bold",            
                                            },        
                                        ),    
                                    ]
                                ),
                                dcc.Graph(id="bar1", figure=fig1)],
                            id="chart1",
                            className="pretty_container",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    style={
                                        "display": "flex",
                                        "justify-content": "center",
                                        "align-items": "center"
                                    },
                                    children=[
                                        html.H6(            
                                            "Gender of Commenters",
                                            style={                
                                                "margin-top": "20",                
                                                "font-weight": "bold",            
                                            },        
                                        ),    
                                    ]
                                ),
                                dcc.Graph(id="bar2", figure=fig2)],
                            id="chart2",
                            className="pretty_container",
                        ),
                        html.Div(
                            [
                                html.P(
                                    text1,
                                    style={
                                        "text-align": "justified",
                                        #"font-size": "10pt"
                                        "margin-left": "20px",
                                        "margin-top": "10px",
                                        },
                                ),
                            ], className="mini_container",
                        ), 
                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H4(
                                            "Video 1 - Opinion Summary",
                                            style={
                                                "margin-top": "0",
                                                "font-weight": "bold",
                                                "text-align": "left",
                                                "margin-left": "15px",
                                            },
                                        ),
                                        html.Div(
                                            [    
                                                html.Div(
                                                    [
                                                        dcc.Graph(
                                                            id="sunburst1",
                                                            figure=sun1,
                                                            className="no-background"
                                                        ),
                                                        html.P(
                                                            vdo1_text1,
                                                            style={
                                                                "text-align": "justified",
                                                                #"font-size": "10pt"
                                                                "margin-left": "20px",
                                                                "margin-top": "10px",
                                                            },
                                                        ),
                                                    ],
                                                    id="vdo1chart1",
                                                    #className="pretty_container",
                                                    style={'flex': 1},
                                                ),
                                                html.Div(
                                                    [
                                                        html.Div(
                                                            [dcc.Graph(id="vdo1bar", figure=vdo1bar,style={'width': '80vh'})],
                                                            id="vdo1chart2",
                                                            className="no-background",
                                                        ),
                                                        html.P(vdo1_text2,
                                                        style={
                                                            "text-align": "justified",
                                                            #"font-size": "10pt"
                                                            "margin-left": "20px",
                                                            "margin-top": "10px",
                                                            },
                                                        ),
                                                    ],
                                                    id="vdo1chart_and_text",
                                                    #className="pretty_container",
                                                    style={
                                                        'flex': 1,
                                                    },
                                                ),
                                            ],
                                            className="row container-display",
                                        ),
                                    ],
                                ),
                            ],
                            id="vdo1_sum",
                            className="pretty_container",
                            style={'display': 'flex'},
                        ),
                    ],  
                ),
            ],
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H4(
                                            "Video 2 - Opinion Summary",
                                            style={
                                                "margin-top": "0",
                                                "font-weight": "bold",
                                                "text-align": "left",
                                                "margin-left": "15px",
                                            },
                                        ),
                                        html.Div(
                                            [    
                                                html.Div(
                                                    [
                                                        dcc.Graph(
                                                            id="sunburst2",
                                                            figure=sun2,
                                                            className="no-background"
                                                        ),
                                                        html.P(
                                                            vdo2_text1,
                                                            style={
                                                                "text-align": "justified",
                                                                #"font-size": "10pt"
                                                                "margin-left": "20px",
                                                                "margin-top": "10px",
                                                            },
                                                        ),
                                                    ],
                                                    id="vdo2chart1",
                                                    #className="pretty_container",
                                                    style={'flex': 1},
                                                ),
                                                html.Div(
                                                    [
                                                        html.Div(
                                                            [dcc.Graph(id="vdo2bar", figure=vdo2bar,style={'width': '80vh'})],
                                                            id="vdo2chart2",
                                                            className="no-background",
                                                        ),
                                                        html.P(vdo2_text2,
                                                        style={
                                                            "text-align": "justified",
                                                            #"font-size": "10pt"
                                                            "margin-left": "20px",
                                                            "margin-top": "10px",
                                                            },
                                                        ),
                                                    ],
                                                    id="vdo2chart_and_text",
                                                    #className="pretty_container",
                                                    style={
                                                        'flex': 1,
                                                    },
                                                ),
                                            ],
                                            className="row container-display",
                                        ),
                                    ],
                                ),
                            ],
                            id="vdo2_sum",
                            className="pretty_container",
                            style={'display': 'flex'},
                        ),
                    ],  
                ),
            ],
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H4(
                                            "Video 3 - Opinion Summary",
                                            style={
                                                "margin-top": "0",
                                                "font-weight": "bold",
                                                "text-align": "left",
                                                "margin-left": "15px",
                                            },
                                        ),
                                        html.Div(
                                            [    
                                                html.Div(
                                                    [
                                                        dcc.Graph(
                                                            id="sunburst3",
                                                            figure=sun3,
                                                            className="no-background"
                                                        ),
                                                        html.P(
                                                            vdo3_text1,
                                                            style={
                                                                "text-align": "justified",
                                                                #"font-size": "10pt"
                                                                "margin-left": "20px",
                                                                "margin-top": "10px",
                                                            },
                                                        ),
                                                    ],
                                                    id="vdo3chart1",
                                                    #className="pretty_container",
                                                    style={'flex': 1},
                                                ),
                                                html.Div(
                                                    [
                                                        html.Div(
                                                            [dcc.Graph(id="vdo3bar", figure=vdo3bar,style={'width': '80vh'})],
                                                            id="vdo3chart2",
                                                            className="no-background",
                                                        ),
                                                        html.P(vdo3_text2,
                                                        style={
                                                            "text-align": "justified",
                                                            #"font-size": "10pt"
                                                            "margin-left": "20px",
                                                            "margin-top": "10px",
                                                            },
                                                        ),
                                                    ],
                                                    id="vdo3chart_and_text",
                                                    #className="pretty_container",
                                                    style={
                                                        'flex': 1,
                                                    },
                                                ),
                                            ],
                                            className="row container-display",
                                        ),
                                    ],
                                ),
                            ],
                            id="vdo3_sum",
                            className="pretty_container",
                            style={'display': 'flex'},
                        ),
                    ],  
                ),
            ],
        ),
        html.Div(
            [
                html.H6(
                    "Summary",
                    style={
                    "margin-top": "0",
                    "font-weight": "bold",
                    "text-align": "center",
                    },
                ),
                html.P(
                    text_sum,
                    style={
                        #"display": "flex",
                        #"align-items": "center",
                        #"text-align": "center",
                        "font-size": "10pt"
                    },
                ),
            
            ], className="mini_container",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6(
                                            "Authors",
                                            style={
                                                "margin-top": "0",
                                                "font-weight": "bold",
                                                "text-align": "center",
                                            },
                                        ),
                                        dcc.Markdown(
                                            """\
                                                - Sirirat Lueprasert (6420412008@stu.nida.ac.th)
                                                - Adcharaporn Thailawan (6420412011@stu.nida.ac.th)
                                                - Supisra Udomlarp (6420412013@stu.nida.ac.th)
                                                """,
                                            style={"font-size": "10pt"},
                                        ),
                                    ], className="mini_container",
                                ),
                                html.Div(
                                    [
                                        html.H6(
                                            "Data Retrived Time",
                                            style={
                                                "margin-top": "0",
                                                "font-weight": "bold",
                                                "text-align": "center",
                                            },
                                        ),
                                        dcc.Markdown(
                                            """\
                                                - Video 1: Wed Jan 04 2023 12:32:31 GMT+0700 (Indochina Time)
                                                - Video 2: Tue Jan 10 2023 02:11:00 GMT+0700 (Indochina Time)
                                                - Video 3: Tue Jan 10 2023 21:38:00 GMT+0700 (Indochina Time)
                                                """,
                                            style={"font-size": "10pt"},
                                        ),
                                    ], className="mini_container",
                                ),
                                html.Div(
                                    [
                                        html.H6(
                                            "Published Date",
                                            style={
                                                "margin-top": "0",
                                                "font-weight": "bold",
                                                "text-align": "center",
                                            },
                                        ),
                                        html.P(
                                            "16 Jan 2023",
                                            style={
                                                #"display": "flex",
                                                #"align-items": "center",
                                                "text-align": "center",
                                                "font-size": "10pt"
                                                },
                                        ),
                                    ], className="mini_container",
                                ),   
                            ], className="row container-display"
                        ),
                    ], className="pretty-container",
                ),
            ], 
            className="row flex-display",
            style={
                "display": "flex",
                "justify-content": "center",
                "align-items": "center"
                }
        ),
    ],
    id="mainContainer",
    className="row flex-display",
    style={"display": "flex", "flex-direction": "column"},
)

server = app.server

if __name__ == '__main__':
    app.run_server(debug=False)