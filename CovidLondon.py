import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import datetime
import imageio

# set the filepath and load in a shapefile
fp = 'London_Borough_Excluding_MHW.shp'
map_df = gpd.read_file(fp)
# check data type so we can see that this is not a normal dataframe, but a GEOdataframe
print(map_df.head())

map_df.plot()

pop_df = pd.read_csv('phe_cases_london_boroughs.csv', header=0)


pop_df['date'] = pd.to_datetime(pop_df['date'])
#data = pop_df.rename(columns={'Homes_Owned_outright,_(2014)_%':'Homes Owned'})

merged = map_df.set_index('NAME').join(pop_df.set_index('area_name'))

variable = 'new_cases'
start_date = pd.to_datetime('20-04-2020')

def plot(day_count):

    data = merged[merged['date']==start_date+datetime.timedelta(days=day_count)]


    
    # set a variable that will call whatever column we want to visualise on the map
   
    # set the range for the choropleth
    #vmin, vmax = 0, 220
    # create figure and axes for Matplotlib
    fig, ax = plt.subplots(1, figsize=(10, 6))
    
    # create map
    
    
    fig.canvas.draw()       # draw the canvas, cache the renderer
    image = data.plot(column=variable, cmap='Greens', linewidth=0.8, ax=ax, edgecolor='0.8')
    image  = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    #return data.plot(column=variable, cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8')
    return image

kwargs_write = {'fps':1.0, 'quantizer':'nq'}
imageio.mimsave('test_map.gif', [plot(i) for i in range(30)], fps=2)