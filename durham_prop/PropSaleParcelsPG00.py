import psycopg2,sys
from psycopg2.extensions import AsIs
import numpy as np
import pandas as pd

def propsaleparcels(begindate,enddate,datadate,featuretype):
    # Define variables
    table_suffix = featuretype+'_'+datadate
    if len(datadate) == 6:
        if featuretype == 'bgs':
            census_table = 'cenbg2010ft'
        elif featuretype == 'trts':
            census_table = 'centr2010ft'
        else:
            sys.exit('Incorrect feature type')
        geoid_yr = 'geoid10'
        parcel_table = 'parcels_org_'+datadate
        feature_id = 'geoid10'
        parcel_id = 'parcel_id'
        date_sold = 'date_sold'
        sale_price = 'sale_price'
        land_use = 'land_use'
        date_sold = 'date_sold'
        owner_name = 'owner_name'
        owner_addr = 'owner_addr'
        site_addr = 'site_addre'
    elif len(datadate) == 4:
        if datadate == '2001':
            if featuretype == 'bgs00':
                census_table = 'cenbg2000ft'
                feature_id = 'bgroup'
                geoid_yr = 'geoid00'
            elif featuretype == 'bgs':
                census_table = 'cenbg2010ft'
                feature_id = 'geoid10'
                geoid_yr = 'geoid10'
            elif featuretype == 'trts00':
                census_table = 'centr2000ft'
                feature_id = 'centract'
                geoid_yr = 'geoid00'
            elif featuretype == 'trts':
                census_table = 'centr2010ft'
                feature_id = 'geoid10'
                geoid_yr = 'geoid10'
            else:
                sys.exit('Incorrect feature type')

            parcel_table = 'durhamparcelhistory'+datadate
            parcel_id = 'akpar_'
            sale_price = 'amslam'
            land_use = 'akrdc1'
            date_sold = 'amdtsl'
            owner_name = 'ownam1'
            owner_addr = 'owadr1'
            site_addr = "akpst_ || ' ' || parcels.akpstn || ' ' || parcels.akpstp"
        elif datadate == '2010':
            if featuretype == 'bgs':
                census_table = 'cenbg2010ft'
            elif featuretype == 'trts':
                census_table = 'centr2010ft'
            else:
                sys.exit('Incorrect feature type')

            geoid_yr = 'geoid10'
            parcel_table = 'durham'+datadate+'_jan_01_parcels'
            feature_id = 'geoid10'
            parcel_id = 'akpar_'
            sale_price = 'amslam'
            land_use = 'akrdc1'
            date_sold = 'amdtsl'
            owner_name = 'ownam1'
            owner_addr = 'owadr1'
            site_addr = "akpst_ || ' ' || akpstn || ' ' || akpstp"
        else:
            sys.exit('Need to check datadate')
    else:
        sys.exit('datadate has incorrect length')

    columns = ['parcelid','geoid','lonlat','latestsaledate','latestsaleprice','ownername','owneraddr','siteaddr']

    # Aggrigates parcel property sales to Census block-groups.
    conn = None
    try:
        conn = psycopg2.connect("dbname='durham_prop' user='jmcmanus' password='bulldurham'")
        cur = conn.cursor()
        cur.execute("""SELECT
            parcels10.%(parcelid)s AS parcel_id,
            feature.%(featureid)s AS geoid,
            ST_AsX3D(ST_Transform(ST_SetSRID(ST_Centroid(parcels.geom), 3632), 4326)) AS lonlat,
            parcels.%(datesold)s AS date_sold,
            parcels.%(saleprice)s AS sale_price,
            parcels.%(ownername)s AS owner_name,
            parcels.%(owneraddr)s AS owner_addr,
            parcels.%(siteaddr)s AS site_addr
        FROM %(censustable)s AS feature
        JOIN %(table_name)s AS parcels
        ON ST_Within(ST_Centroid(parcels.geom), feature.geom)
        JOIN durham2010_jan_01_parcels AS parcels10
        ON parcels.akpar_=parcels10.old_id
        WHERE
            feature.%(featureid)s LIKE '37063%%' AND
            parcels.%(landuse)s = '111' AND
            parcels.%(saleprice)s > 0 AND
            parcels.%(datesold)s BETWEEN %(begin_date)s AND %(end_date)s
        ORDER BY geoid""",
        {'begin_date':begindate,'end_date':enddate,'table_name':AsIs(parcel_table),'censustable':AsIs(census_table),'featureid':AsIs(feature_id),'datesold':AsIs(date_sold),'saleprice':AsIs(sale_price),'landuse':AsIs(land_use),'datesold':AsIs(date_sold),'ownername':AsIs(owner_name),'owneraddr':AsIs(owner_addr),'siteaddr':AsIs(site_addr),'parcelid':AsIs(parcel_id)})

        rows = cur.fetchall()
        data = pd.DataFrame(rows, columns=columns)
        data['lon'], data['lat'] = data.lonlat.str.split(' ', 1).str
        data.drop(['lonlat'], axis=1, inplace=True)

        data.to_csv('propsaleparcels'+featuretype+begindate+'-'+enddate+'.csv', sep='|',index=False)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Runs the programs.
propsaleparcels("19980101","20001231","2001","bgs10")
#propsaleparcels("19980101","20001231","2001","bgs")
