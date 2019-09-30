import plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
import pandas as pd
import cufflinks as cf
py.offline.init_notebook_mode(connected=True)
cf.go_offline()


df = pd.read_csv('2014_World_GDP')

df_head = df.head()

data = dict(type= 'choropleth',
locations = df['CODE'],
z = df['GDP (BILLIONS)'],
text = df['COUNTRY'],
colorbar = {'title':'GDP in Billion USD'}
)

layout = dict(title = '2014 Global GDP',
geo = dict(showframe = False),

)
choromap3 = go.Figure(data=[data], layout=layout)

py.offline.plot(choromap3, filename='choro.html')

iplot(choromap3)

