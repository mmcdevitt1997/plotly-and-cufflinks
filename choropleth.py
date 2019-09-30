import plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
import cufflinks as cf
py.offline.init_notebook_mode(connected=True)
cf.go_offline()

data = dict(type='choropleth',
            locations=['AZ', 'CA', 'NY'],
            locationmode='USA-states',
            colorscale='Portland',
            text=['text1', 'text2', 'text3'],
            z=[1.0, 2.0, 3.0],
            colorbar={'title': 'Colorbar Title here'})

layout = dict(geo={'scope': 'usa'})

choromap = go.Figure(data=[data], layout=layout)

py.offline.plot(choromap, filename='choro.html')

iplot(choromap)
