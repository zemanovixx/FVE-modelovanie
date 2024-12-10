import plotly.graph_objects as go 
from plotly.subplots import make_subplots

def weather(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['datetime'],
        y=df['Gg_pyr'],
        name='Gg_pyr'
    ))
    
    fig.add_trace(go.Scatter(
        x=df['datetime'],
        y=df['Gg_si_east'],
        name='Gg_si_east'
    ))
    
    fig.add_trace(go.Scatter(
        x=df['datetime'],
        y=df['Gg_si_west'],
        name='Gg_si_west'
    ))
    
    fig.show()


def power_dc(df_dc,df_consumption):
    fig = make_subplots(
        rows=2,
        cols=2
    )

    fig.add_trace(go.Scatter(
        x=df_dc['datetime'],
        y=df_dc['i_mp'],
        name='i_mp'
    ),
        row=1,
        col=1
    )

    fig.add_trace(go.Scatter(
        x=df_dc['datetime'],
        y=df_dc['i_sc'],
        name='i_sc'
    ),
        row=1,
        col=1
    )

    fig.add_trace(go.Scatter(
        x=df_dc['datetime'],
        y=df_dc['v_oc'],
        name='v_oc'
    ),
        row=1,
        col=2
    )

    fig.add_trace(go.Scatter(
        x=df_dc['datetime'],
        y=df_dc['v_mp'],
        name='v_mp'
    ),
        row=1,
        col=2
    )
    
    fig.add_trace(go.Scatter(
        x=df_dc['datetime'],
        y=df_dc['p_mp'],
        name='p_mp'
    ),
        row=2,
        col=1
    )

    # fig.add_trace(go.Scatter(
    #     x=df_dc['datetime'],
    #     y=df_dc['i_x'],
    #     name='i_x'
    # ),
    #     row=2,
    #     col=2
    # )

    # fig.add_trace(go.Scatter(
    #     x=df_dc['datetime'],
    #     y=df_dc['i_xx'],
    #     name='i_xx'
    # ),
    #     row=2,
    #     col=2
    # )

    fig.add_trace(go.Scatter(
        x=df_consumption['datetime']  ,
        y=df_consumption['Consumption_W'],
        name='Consumption_W'
    ),
        row=2,
        col=2
    )

    fig.add_trace(go.Scatter(
        x=df_dc['datetime'],
        y=df_dc['p_mp'],
        name='vykon'
    ),
        row=2,
        col=2
    )

    fig.update_xaxes(title_text = 'Dátum a čas',row = 1  , col = 1 )
    fig.update_xaxes(title_text = 'Dátum a čas',row = 2  , col = 1 )
    fig.update_xaxes(title_text = 'Dátum a čas',row = 1  , col = 2 )
    fig.update_xaxes(title_text = 'Dátum a čas',row = 2  , col = 2 )

    fig.update_yaxes(title_text = 'prud I [A]',row = 1 , col = 1 )
    fig.update_yaxes(title_text = 'Napetie U [V]',row = 1 , col = 2 )
    fig.update_yaxes(title_text = 'Vykon DC [W]',row = 2 , col = 1 )
    fig.update_yaxes(title_text = 'prud I .....[A]',row = 2 , col = 2 )



    fig.show()

def power_ac(df,df_consumption):
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['datetime'],
        y=df['ac'],
        name='ac'
    ))

    fig.add_trace(go.Scatter(
    x=df_consumption['datetime']  ,
    y=df_consumption['Consumption_W'],
    name='Consumption_W'
    ))
    
    fig.update_layout(
        title = 'Výkon AC',
        xaxis_title = 'Dátum a čas',
        yaxis_title = 'AC [W]'
    )

    fig.show()





def energy(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
            x = df['datetime'],
        y = df['ac'],
        name = 'AC vykon' 
    ))
    
    fig.add_trace(go.Scatter(
        x = df['datetime'],
        y = df['surplus'],
        name = 'prebytok' 
    ))

    fig.add_trace(go.Scatter(
        x=df['datetime'],
        y= df['battery_SOC']
    ))
    fig.show()