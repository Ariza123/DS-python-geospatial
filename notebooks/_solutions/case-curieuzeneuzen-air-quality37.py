gdf['land_use'] = rasterstats.point_query(gdf_raster.geometry, "data/CLC2018_V2020_20u1_flanders.tif", interpolate='nearest')