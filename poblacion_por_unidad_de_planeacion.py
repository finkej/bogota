import pandas as pd
import geopandas as gpd

#import data data from census
poblacion_data_link='https://raw.githubusercontent.com/finkej/bogota/master/estadisticas_poblacion/Informaci_n_poblacional_Encuesta_Multiprop_sito_Bogot__2017.csv'
df=pd.read_csv(poblacion_data_link)

gpd.GeoDataFrame(df).rename({'UPZ':'UPlCodigo'})

gdf=gpd.read_file('mapa_bogota/unidad_de_planeacion/unidad_de_planeacion.shp')

# create city boundaries
#crs = {'init': 'epsg:4326'}
# gdf.drop(index=gdf['UPlArea'].idxmax(), inplace=True)
# gdf.drop(index=gdf['UPlArea'].idxmax(), inplace=True)
# gdf.drop(index=gdf['UPlArea'].idxmax(), inplace=True)
# gdf['city']='bogota'
# limite_municipal=gdf.dissolve(by='city')
# limite_municipal.to_file(driver = 'ESRI Shapefile', filename = './mapa_bogota/limite_municipal_urbano/limite_municipal_urbano.shp')


