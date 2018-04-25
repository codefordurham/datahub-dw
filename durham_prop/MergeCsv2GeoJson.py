import geopandas as gpd
import pandas as pd

durhambgs = gpd.read_file('durhambgs.geojson')
#durhambgs.head()

propsales = pd.read_csv('propsales_100517.csv')
#propsales.head()

durhambgs = durhambgs.sort_values('GEOID10').reset_index(drop=True)
propsales = propsales.sort_values('GEOID10').reset_index(drop=True)

durhampropbgs = gpd.GeoDataFrame(pd.concat([durhambgs, propsales], axis=1))
#durhampropbgs = durhambgs.merge(propsales, how='outer', on='geoid10')
#durhampropbgs = gpd.sjoin(durhambgs, propsales, how="inner", op='intersects')

with open('durhampropbgs.geojson', 'w') as f:
    f.write(durhampropbgs.to_json())

