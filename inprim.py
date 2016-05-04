import pandas as pd
import ast
import vincent
import folium
from folium import plugins
import nltk
from nltk.corpus import stopwords
from nltk import FreqDist
from pandas.tseries.resample import TimeGrouper
from pandas.tseries.offsets import DateOffset
indiana = pd.read_csv('D:\Documents\DataIncubator\INprimloc.csv')
indiana['createdat'] = pd.to_datetime(pd.Series(indiana['created_at']))
indiana.set_index('createdat', drop=False, inplace=True)
indiana.index = indiana.index.tz_localize('GMT').tz_convert('EST')
indiana.index = indiana.index - DateOffset(hours = 12)
indiana.index

text = indiana['text']
stop = stopwords.words('english')
tokens = []
for txt in text.values:
    tokens.extend([t.lower().strip(":,.") for t in txt.split()])


filtered_tokens = [w for w in tokens if not w in stop]

freqdist = nltk.FreqDist(filtered_tokens)
freqdist.plot(25)
indiana1m = indiana['created_at'].resample('1t', how='count')
indiana1m.head()

#vincent.core.initialize_notebook()
area = vincent.Area(indiana1m)
area.colors(brew='Spectral')
area.display()
area.to_json('cruz.json', html_out=True, html_path='cruz.html')
#area.savefig('IN.png')
#locations
locations = pd.read_csv('D:\Documents\DataIncubator\INprimloc.csv', usecols=['geo']).dropna()
geos = []

for location in locations.values:
  
  geos.append(ast.literal_eval(location[0])['coordinates'])
  
in_rep= folium.Map(location=[39.0558,-125], zoom_start=4)
heatmap_map = folium.Map(location=[39.0558,-125], zoom_start=4)

for geo in geos:
  in_rep.circle_marker(location=geo, radius=250)
  #hm = plugins.HeatMap(location=geo)
  #heatmap_map.add_children(hm)
in_rep.save('Inrep.html')
#heatmap_map.save('Inrepheat.html')

