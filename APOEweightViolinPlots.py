import plotly.graph_objects as go
import os
import pandas as pd
#from plotly.offline import init_notebook_mode, plot_mpl

#df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/violin_data.csv")

df=pd.read_csv(r"C:\Users\Ana\OneDrive\InVivoMaster_APOE.csv")

print(df['sex'])

fig = go.Figure()

#fig.add_trace(go.Violin(x=df['day'][ df['sex'] == 'Male' ],
#                        y=df['total_bill'][ df['sex'] == 'Male' ],
#                        legendgroup='M', scalegroup='M', name='M',
#                        line_color='blue')
#             )


#print(df.genotype[df['genotype'].isin(['APOE22','APOE33'])])

print(df['genotype'].isin(['APOE22','APOE33']))
df_short=df[df['genotype'].isin(['APOE22','APOE33','APOE44', 'CVN'])]

print(df_short)
fig.add_trace(go.Violin(x=df_short['genotype'] [ df_short['sex'] == 0 ],
                        y=df_short['body_weight'][ df_short['sex'] == 0 ],
                        legendgroup='M', scalegroup='M', name='M',
                        line_color='blue', points='all')
             )
fig.add_trace(go.Violin(x= df_short['genotype'] [ df_short['sex'] == 1 ],
                        y=df_short['body_weight'][ df_short['sex'] == 1 ],
                        legendgroup='F', scalegroup='F', name='F',
                        line_color='orange', points='all')
             )


fig.update_traces(box_visible=True, meanline_visible=True)
fig.update_layout(violinmode='group')
fig.show()

fig.write_image("body_weight.png")