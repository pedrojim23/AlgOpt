import osmnx as ox # Biblioteca para trabajar con los datos de OpenStreetMap
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from scipy.spatial import Voronoi, voronoi_plot_2d

#Lugar a analizar
lugar = 'Oaxaca de Juarez, Mexico'
#Definimos nuestro dataset de las estaciones de bomberos
ds = 'bomb.csv'

#Leemos los datos de ubicación los almacenamos en un DataFrame
df = pd.read_csv(ds)
#Creamos una columna 'geometry' en el DataFrame, que contiene objetos Point a partir de las coordenadas de longitud y latitud
geometry = gpd.points_from_xy(df['longitude'], df['latitude'])
#Creamos un GeoDataFrame a partir del DataFrame y la columna geometry
gdf = gpd.GeoDataFrame(df, geometry=geometry)

#Obtenemos el grafo de oax
G = ox.graph_from_place(lugar, network_type='all')

#Creamos la figura y los ejes para trazar el grafo de la ciudad
area = ox.geocode_to_gdf(lugar)

# plot city graph
'''fig, ax = ox.plot_graph(G, show=False, close=False)
area.plot(ax=ax, facecolor='none', edgecolor='orange')'''

#Creamos el diagrama de Voronoi a partir de las coordenadas de los puntos de ubicación
vor = Voronoi([(p.x, p.y) for p in geometry])
# Trazamos el diagrama de Voronoi sobre el mismo gráfico
#voronoi_plot_2d(vor, show_vertices=False, line_colors='red', point_size=10)

fig, ax = plt.subplots(figsize=(10, 10))
ox.plot_graph(G, ax=ax, show=False, close=False)
area.plot(ax=ax, facecolor='none', edgecolor='orange')
voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='red', line_width=1, point_size=10)
gdf.plot(ax=ax, color='blue', markersize=50, alpha=0.5)
plt.title('Diagrama de Voronoi y Estaciones de Bomberos en {}'.format(lugar))
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.grid(True)
plt.tight_layout()

plt.show()

gdf_proj = ox.projection.project_gdf(gdf)
G = ox.graph_from_place(lugar, network_type='all')
G_proj = ox.project_graph(G)
