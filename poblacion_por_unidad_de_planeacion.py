import pandas as pd
import geopandas as gpd
import geoplot


#import data from census
df1=pd.read_csv('./encuestas/encuesta_multiproposito_bogota_2017.csv')
df1.rename(columns={'UPZ':'UPlCodigo'}, inplace=True)
#gdf1=(gpd.GeoDataFrame(df)).rename(columns={'UPZ':'UPlCodigo'})
#import UP data
gdf=gpd.read_file('./mapa_bogota/unidad_de_planeacion/unidad_de_planeacion.shp')
df2=pd.DataFrame(gdf)
df=pd.merge(df1, df2, on='UPlCodigo')
df.columns=df.columns.str.lower().str.replace(' ','_').str.replace('(','').str.replace(')','').str.replace('ñ','n').str.replace('ó','o')

for column in df.columns:
    if (type(df[column][0]) is str):
        df[column]=df[column].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8').str.lower()
  

gdf=gpd.GeoDataFrame(df)

geoplot.choropleth(
    gdf, hue=gdf['personas'],
    cmap='Greens', figsize=(8, 4)
)

gdf.to_file(driver = 'ESRI Shapefile', filename = './encuestas/encuesta_multiproposito_bogota_2017.shp')

#gdf=gpd.read_file('./encuestas/encuesta_multiproposito_bogota_2017.shp')

# create city boundaries
#crs = {'init': 'epsg:4326'}
# gdf.drop(index=gdf['UPlArea'].idxmax(), inplace=True)
# gdf.drop(index=gdf['UPlArea'].idxmax(), inplace=True)
# gdf.drop(index=gdf['UPlArea'].idxmax(), inplace=True)
# gdf['city']='bogota'
# limite_municipal=gdf.dissolve(by='city')
# limite_municipal.to_file(driver = 'ESRI Shapefile', filename = './mapa_bogota/limite_municipal_urbano/limite_municipal_urbano.shp')