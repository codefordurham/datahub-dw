The commands in this README.md, and the python code in this directory are used to create data sets for the 
Code for Durham, Affordable Housing project. It specifically deals with how to aggregate Durham parcel data
variables to US Census block-groups using PostGIS. It also covers how to then create GeoJson and TopoJson 
files using the aggregated data.

The property parcel data set, for Durham NC, can be downloaded from the NC OneMap GeoSpatial Portal:

    http://data.nconemap.gov/geoportal/catalog/main/home.page

After downloading the file Durham_parcels_2017_10_05.zip unzip it, and then unzip the file 
durham_parcels_2017_10_05_5836.zip inside it.

Then run the shp2pgsql command on the original parcel data, to generate an sql file to ingest into your 
Postgresql database:

shp2pgsql -I -s 3632 Durham_parcels_2017_10_05/durham_parcels_2017_10_05_5836/nc_durham_parcels_original_2017_10_05.shp parcels_org_100517 > parcels_org_100517.sql

Run the following command to ingest the data:

psql -U jmcmanus -d durham_prop -f parcels_org_100517.sql

Replace jmcmanus with you username, and durham_prop of you database.

Download the US Census block-group shape file for North Carolina from:

http://data.nconemap.gov/geoportal/rest/find/document?searchText=Census%20Block&f=html

We are using this data, instead of getting the block-group data from the US Census because it's  
projection is North Carolina state plane, which is the same projection that the Durham parcel 
data is in. However, the Durham parcel data is in feet, and the Census block-group data is in
meters, so you will need to covert it to feet. Start by unzipping the file cenbg2010.zip, and then
create a directory name cenbg2010ft. Then run the following command:

ogr2ogr -f "ESRI Shapefile" cenbg2010ft/cenbg2010.shp cenbg2010/cenbg2010.shp -s_srs EPSG:3631 -t_srs EPSG:3632

You are now ready to create the sql file by running:

shp2pgsql -I -s 3632 cenbg2010ft/cenbg2010.shp cenbg2010 > cenbg2010.sql

and ingest it into you database:

psql -U jmcmanus -d durham_prop -f cenbg2010.sql

Run the PropSalesBG.py program with appropriate dates. This program creates a propsale table in your 
database, and then insert aggrigate statistics, of parcel data into block-groups, into the table.

To extract the property sales data to a csv file run PropSalesExt.py

The create a GeoJson file from the census shape file by running the following org2ogr command:
ogr2ogr -f GeoJSON -t_srs EPSG:4326 -sql "select GEOID10 from cenbg2010 where countyfp10 = '063'" durhambgs.  geojson cenbg2010/cenbg2010.shp

To convert the GeoJson file to TopoJson and merge it with the property sales data issue the following 
command:
topojson -e propsales_100517.csv --id-property=+GEOID10 -p mean_sale_price,tot_sale_price,num_sales,begin_date,end_date --spherical -s 1E-10 -q 1E8 -o durhambgs.topojson durhambgs.geojson

If you want to merge the property sales data with the GeoJson file you should modify and run the
MergeCsv2GeoJson.py python snippet accordingly.
