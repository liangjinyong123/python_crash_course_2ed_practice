# Mapping Global Datasets: GeoJSON Format
## Downloading Earthquake Data
## Examining GeoJSON Data
from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to a Python object.
# path = Path('eq_data/eq_data_1_day_m1.geojson')
# contents = path.read_text()
# all_eq_data = json.loads(contents)

# Create a more readable version of the data file.
# path = Path('eq_data/readable_eq_data.geojson')
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents)

## Making a List of All Earthquakes
# Examine all earthquakes in the dataset.
# all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

## Extracting Magnitudes
# mags = []
# for eq_dict in all_eq_dicts:
#     mag = eq_dict['properties']['mag']
#     mags.append(mag)

# print(mags[:10])

## Extracting Location Data
# mags, lons, lats = [], [], []
# for eq_dict in all_eq_dicts:
#     mag = eq_dict['properties']['mag']
#     lon = eq_dict['geometry']['coordinates'][0]
#     lat = eq_dict['geometry']['coordinates'][1]
#     mags.append(mag)
#     lons.append(lon)
#     lats.append(lat)

# print(mags[:10])
# print(lons[:5])
# print(lats[:5])

## Building a World Map
# title = 'Global Earthquakes'
# fig = px.scatter_geo(lat=lats, lon=lons, title=title)
# fig.show()

## Representing Magnitudes
# Read data as a string and convert to a Python object. 
# path = Path('eq_data/eq_data_30_day_m1.geojson')
# contents = path.read_text()
# all_eq_data = json.loads(contents)

# all_eq_dicts = all_eq_data['features']

# mags, lons, lats = [], [], []
# for eq_dict in all_eq_dicts:
#     mag = eq_dict['properties']['mag']
#     lon = eq_dict['geometry']['coordinates'][0]
#     lat = eq_dict['geometry']['coordinates'][1]
#     mags.append(mag)
#     lons.append(lon)
#     lats.append(lat)

# title = 'Global Earthquakes'
# fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title)
# fig.show()

## Customizing Marker Colors
# fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
#         color=mags,
#         color_continuous_scale='Viridis',
#         labels={'color': 'Magnitude'},
#         projection='natural earth',
#     )
# fig.show()

## Other Color Scales
# print(px.colors.named_colorscales())

## Adding Hover Text
path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title)
fig.show()

# Customizing Marker Colors
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
        color=mags,
        color_continuous_scale='Viridis',
        labels={'color': 'Magnitude'},
        projection='natural earth',
        hover_name=eq_titles,
    )
fig.show()