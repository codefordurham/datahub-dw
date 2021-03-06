import psycopg2,sys
import numpy as np
from psycopg2.extensions import AsIs

def createpropsale(datadate,featuretype):
    # Define variables
    table_suffix = featuretype+'_'+datadate
    if len(datadate) == 6:
        geoid_yr = 'geoid10'
    elif len(datadate) == 4:
        if datadate == '2001':
            if featuretype == 'trts00':
                geoid_yr = 'geoid00'
            elif featuretype == 'trts':
                geoid_yr = 'geoid10'
            elif featuretype == 'bgs':
                geoid_yr = 'geoid00'
            else:
                sys.exit('Incorrect featureid')
        elif datadate == '2010':
            geoid_yr = 'geoid10'
        else:
            sys.exit('Need to check datadate')
    else:
        sys.exit('datadate has incorrect length')

    # Creates propsales table.
    conn = None
    try:
        conn = psycopg2.connect("dbname='durham_prop' user='jmcmanus' password='bulldurham'")
        cur = conn.cursor()
        cur.execute("""SET CLIENT_ENCODING TO UTF8""")
        cur.execute("""SET STANDARD_CONFORMING_STRINGS TO ON""")
        cur.execute("""BEGIN""")
        cur.execute("""CREATE TABLE %(table_name)s (gid serial,
                          %(geoid)s varchar(255),
                          mean_sale_price float8,
                          min_sale_price float8,
                          max_sale_price float8,
                          median_sale_price float8,
                          stddev_sale_price float,
                          total_sale_price float8,
                          num_sales int,
                          begin_date date,
                          end_date date)""",
                          {'table_name': AsIs('propsales_'+table_suffix),'geoid':AsIs(geoid_yr)})
        cur.execute("""ALTER TABLE %(table_name)s ADD PRIMARY KEY (gid)""",
                {'table_name': AsIs('propsales_'+table_suffix),'geoid':AsIs(geoid_yr)})

        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insertpropsale(begindate,enddate,datadate,featuretype):
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
        sale_price = 'sale_price'
        land_use = 'land_use'
        date_sold = 'date_sold'
    elif len(datadate) == 4:
        if datadate == '2001':
            if featuretype == 'bgs':
                census_table = 'cenbg2000ft'
                feature_id = 'bgroup'
                geoid_yr = 'geoid00'
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
            sale_price = 'amslam'
            land_use = 'akrdc1'
            date_sold = 'amdtsl'
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
            sale_price = 'amslam'
            land_use = 'akrdc1'
            date_sold = 'amdtsl'
        else:
            sys.exit('Need to check datadate')
    else:
        sys.exit('datadate has incorrect length')

    # Aggrigates parcel property sales to Census block-groups.
    conn = None
    try:
        conn = psycopg2.connect("dbname='durham_prop' user='jmcmanus' password='bulldurham'")
        cur = conn.cursor()
        """CREATE OR REPLACE FUNCTION _final_median(NUMERIC[])
                       RETURNS NUMERIC AS
                       $$
                         SELECT AVG(val)
                         FROM (
                               SELECT val
                               FROM unnest($1) val
                               ORDER BY 1
                               LIMIT  2 - MOD(array_upper($1, 1), 2)
                               OFFSET CEIL(array_upper($1, 1) / 2.0) - 1
                              ) sub;
                       $$
                       LANGUAGE 'sql' IMMUTABLE;
                       CREATE AGGREGATE median(NUMERIC) (
                         SFUNC=array_append,
                         STYPE=NUMERIC[],
                         FINALFUNC=_final_median,
                         INITCOND='{}'
                       );"""

        cur.execute("""SELECT
            feature.%(featureid)s AS geoid,
            AVG(parcels.%(saleprice)s) AS mean_sale_price,
            MIN(parcels.%(saleprice)s) AS min_sale_price,
            MAX(parcels.%(saleprice)s) AS max_sale_price,
            MEDIAN(parcels.%(saleprice)s) AS median_sale_price,
            STDDEV_SAMP(parcels.%(saleprice)s) AS stddev_sale_price,
            SUM(parcels.%(saleprice)s) AS total_sale_price,
            COUNT(parcels.%(saleprice)s) AS num_sales
        FROM %(censustable)s AS feature
        JOIN %(table_name)s AS parcels
        ON ST_Within(ST_Centroid(parcels.geom), feature.geom)
        WHERE
            feature.%(featureid)s LIKE '37063%%' AND
            parcels.%(landuse)s = '111' AND
            parcels.%(saleprice)s > 0 AND
            parcels.%(datesold)s BETWEEN %(begin_date)s AND %(end_date)s
        GROUP BY feature.%(featureid)s
        ORDER BY mean_sale_price""",
        {'begin_date':begindate,'end_date':enddate,'table_name':AsIs(parcel_table),'censustable':AsIs(census_table),'featureid':AsIs(feature_id),'saleprice':AsIs(sale_price),'landuse':AsIs(land_use),'datesold':AsIs(date_sold)})

        rows = cur.fetchall()

        cur.execute("SET CLIENT_ENCODING TO UTF8")
        cur.execute("SET STANDARD_CONFORMING_STRINGS TO ON")
        cur.execute("BEGIN")

        for row in rows:
            if row[5] == None:
                cur.execute("INSERT INTO propsales_"+table_suffix+" (%(geoid)s,mean_sale_price,min_sale_price,max_sale_price,median_sale_price,      stddev_sale_price,total_sale_price,num_sales,begin_date,end_date) VALUES ('"+row[0]+"','"+str(row[1])+"','"+str(row[2])+"','"+str(row[3])+"','"+      str(row[4])+"','"+"NaN"+"','"+str(row[6])+"','"+str(row[7])+"','"+begindate+"','"+enddate+"')",{'geoid':AsIs(geoid_yr)})
            else:
                cur.execute("INSERT INTO propsales_"+table_suffix+" (%(geoid)s,mean_sale_price,min_sale_price,max_sale_price,median_sale_price,stddev_sale_price,total_sale_price,num_sales,begin_date,end_date) VALUES ('"+row[0]+"','"+str(row[1])+"','"+str(row[2])+"','"+str(row[3])+"','"+str(row[4])+"','"+str(row[5])+"','"+str(row[6])+"','"+str(row[7])+"','"+begindate+"','"+enddate+"')",{'geoid':AsIs(geoid_yr)})

        cur.execute("COMMIT")
        cur.execute("ANALYZE %(table_name)s",{'table_name': AsIs('propsales_'+table_suffix)})

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Runs the programs.
createpropsale("011818","bgs")
insertpropsale("20151001","20171231","011818","bgs")
createpropsale("100517","bgs")
insertpropsale("20130101","20141231","100517","bgs")
createpropsale("2001","bgs")
insertpropsale("19980101","20001231","2001","bgs")
createpropsale("2001","trts00")
insertpropsale("19980101","20001231","2001","trts00")
createpropsale("2001","trts")
insertpropsale("19980101","20001231","2001","trts")
createpropsale("2010","trts")
insertpropsale("20081001","20091231","2010","trts")
createpropsale("100517","trts")
insertpropsale("20130101","20141231","100517","trts")
createpropsale("011818","trts")
insertpropsale("20151001","20171231","011818","trts")

