import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("About", href="/about")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu",
            children=[
                dbc.DropdownMenuItem("Analytics", href = "/analytics"),
                dbc.DropdownMenuItem("Data Science", href="/datascience"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Predictive", href="/predictive"),
            ],
        ),
    ],
    brand="PGC Data Designs",
    brand_href="/",
    sticky="top",
)

analytics = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Heading"),
                        html.P(
                            """\
Donec id elit non mi porta gravida at eget metus.
Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum
nibh, ut fermentum massa justo sit amet risus. Etiam porta sem
malesuada magna mollis euismod. Donec sed odio dui. Donec id elit non
mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus
commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit
amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed
odio dui."""
                        ),
                        dbc.Button("View details", color="secondary"),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.H2("Graph"),
                        dcc.Graph(
                            figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                        ),
                    ]
                ),
            ]
        )
    ],
    className="mt-4",
)

datascience = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [html.H2("A simple graph"),
                     html.P("""This simple graph is here to demonstrate that you can use
                    dash and bootstap to create analytical web applications with style. There are
                   a few libraries that help accomplish this. Dash-bootstrap-components contains the
                   modules required for bootstrap styling, dash and dash core components along with dash html
                   contain the rest needed."""),
                     dbc.Button("about", color="secondary"),
                    ],md=4,
                    ),
                dbc.Col(
                    [html.H2("Graph"),
                             dcc.Graph(id='example2',
                                figure={
                                    'data': [
                                        {'x': [1, 2, 3, 4, 5], 'y': [3, 5, 9, 3, 4], 'type': 'line', 'name': 'Boats'},
                                        {'x': [1, 2, 3, 4, 5], 'y': [6, 5, 7, 1, 9], 'type': 'line', 'name': 'Cars'},
                                    ],
                                    
                                })
                        ])
            ])
 
    ], className='mt-4')



app.layout = html.Div([navbar, dcc.Location(id='url', refresh=False),html.Div(id='page-content')])

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/' or pathname == '/analytics' :
        return analytics
    elif pathname == '/datascience':
        return datascience
    else:
        return noPage


if __name__ == "__main__":
    app.run_server(debug=True)
