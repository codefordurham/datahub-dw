The commands in this README.md, and the python code in this directory are used to create data sets 
for the Code for Durham, Affordable Housing project. It specifically deals with how to aggregate 
Durham parcel data variables to US Census block-groups using PostGIS. It also covers how to then 
create GeoJson and TopoJson files using the aggregated data.

The property parcel data set, for Durham NC, can be downloaded from the NC OneMap GeoSpatial Portal:

    http://data.nconemap.gov/geoportal/catalog/main/home.page

After downloading the file Durham_parcels_2017_10_05.zip unzip it, and then unzip the file 
durham_parcels_2017_10_05_5836.zip inside it.

Then run the shp2pgsql command on the original parcel data, to generate an sql file to ingest into 
your Postgresql database:

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

To create the Single Family Housing owner ship data, do thing as above but use the programs 
SingFamHouseBG.py and SingFamHouseExt.py, respectively.

To create a GeoJson (durhambgs.geojson) file from the census shape file runn the following org2ogr 
command:

ogr2ogr -f GeoJSON -t_srs EPSG:4326 -sql "select GEOID10 from cenbg2010 where countyfp10 = '063'" durhambgs.geojson cenbg2010/cenbg2010.shp

To create a topojson file (durhambgs.topojson) from the GeoJson file run the following command:

topojson --spherical -s 1E-10 -q 1E8 --id-property=GEOID10 -o durhambgs.topojson durhambgs.geojson

To convert the GeoJson file to TopoJson and merge (durhampropbgs.topojson) it with the property sales 
data run the following command:

topojson -e propsales_100517.csv --id-property=+GEOID10 -p msp2015,tsp2015,ns2015,msp2016,tsp2016,ns2016 --spherical -s 1E-10 -q 1E8 -o durhambgs.topojson durhambgs.geojson

If you want to merge the property sales data with the GeoJson file you should modify and run the
MergeCsv2GeoJson.py python snippet accordingly.

The next step is to make a view table of the propsale table and a table that contains Durham Compass 
data. You can get the Durham Compass data at: http://compass.durhamnc.gov/

The Durham Neighborhood Compass is a quantitative indicators project with qualitative values, integrating data from local government, the Census Bureau and other state and federal agencies. Measurements are identified through local strategic planning, resident input, research and best practices for neighborhood indicators. The project objective is to provide data that allows all local stakeholders to track quality of life and provision of services throughout Durham.

Use the same methods described previously on how to ingest shp file data into the postgresql data base. The use the following SQL command to creat the view table:

CREATE VIEW propsalecompass AS
    SELECT PS.geoid10, PS.mean_sale_price, PS.min_sale_price, PS.max_sale_price,
           PS.median_sale_price, PS.total_sale_price, PS.num_sales,
           CAST(DC.mhi_13 AS DECIMAL)+CAST(DC.mhi_14 AS DECIMAL)/2.0 AS mhi,
           CAST(PS.median_sale_price AS DECIMAL)/(CAST(DC.mhi_13 AS DECIMAL)+CAST(DC.mhi_14 AS DECIMAL)/2.0) AS pir,
           PS.begin_date, PS.end_date
    FROM propsales_100517 AS PS
    INNER JOIN durhamcompass AS DC ON (PS.geoid10=DC.geoid10);

Assuming the propsal table in named propsales_100517 and Durham Compass table is named durhamcompass.

Now use the file PropSalesCompassExt.py to extract the data into a csv file. The csv files can be imported into the appropriate tables in the datahub-be database, where they can be served using the
Django Rest Framework. To learn more about the datahub-be project go to the following GitHub repository:

https://github.com/codefordurham/datahub-be