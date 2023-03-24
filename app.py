import pandas as pd
import panel as pn
import hvplot.pandas

df = pd.DataFrame([['A','B','C','D'],[1,2,3,4],[4,6,9,10],[9,30,45,23],[5,30,23,13]]).T
df.columns=['x','y1','y2','y3','y4']

# Define the dashboard layout
pn.extension()
dashboard = pn.Column(
    '## Dashboard Title',
    pn.Row(
        df.hvplot.line('x', 'y1', label='Line 1', legend='bottom_left') +
        df.hvplot.line('x', 'y2', label='Line 2', legend='bottom_left'),
    ),
    pn.Row(
        df.hvplot.scatter('x', 'y3', label='Scatter', legend='bottom_left') +
        df.hvplot.bar('x', 'y4', label='Bar', legend='bottom_left'),
    ),
)

# Display the dashboard
dashboard.servable()
