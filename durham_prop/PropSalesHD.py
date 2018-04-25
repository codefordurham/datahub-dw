import psycopg2
from psycopg2.extensions import AsIs

def createpropsale(datadate):
    # Creates propsales table.
    conn = None
    try:
        conn = psycopg2.connect("dbname='durham_prop' user='jmcmanus' password='bulldurham'")
        cur = conn.cursor()
        cur.execute("""SET CLIENT_ENCODING TO UTF8""")
        cur.execute("""SET STANDARD_CONFORMING_STRINGS TO ON""")
        cur.execute("""BEGIN""")
        cur.execute("""CREATE TABLE %(table_name)s (gid serial,
                          objectid varchar(255),
                          mean_sale_price float8,
                          min_sale_price float8,
                          max_sale_price float8,
                          median_sale_price float8,
                          stddev_sale_price float8,
                          total_sale_price float8,
                          num_sales int,
                          begin_date date,
                          end_date date)""",
                          {'table_name': AsIs('propsales_hds_'+datadate)})
        cur.execute("""ALTER TABLE %(table_name)s ADD PRIMARY KEY (gid)""",
                   {'table_name': AsIs('propsales_hds_'+datadate)})

        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insertpropsale(begindate,enddate,datadate):
    # Aggrigates parcel propert sales to Census block-groups.
    conn = None
    try:
        conn = psycopg2.connect("dbname='durham_prop' user='jmcmanus' password='bulldurham'")
        cur = conn.cursor()
        #cur.execute(
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
        #)

        cur.execute("""SELECT
            hds.objectid AS objectid,
            AVG(parcels.sale_price) AS mean_sale_price,
            MIN(parcels.sale_price) AS min_sale_price,
            MAX(parcels.sale_price) AS max_sale_price,
            MEDIAN(parcels.sale_price) AS median_sale_price,
            STDDEV_SAMP(parcels.sale_price) AS stddev_sale_price,
            SUM(parcels.sale_price) AS total_sale_price,
            COUNT(parcels.sale_price) AS num_sales
        FROM neighborhoods_ft AS hds
        JOIN %(table_name)s AS parcels
        ON ST_Within(ST_Centroid(parcels.geom), hds.geom)
        WHERE
            parcels.land_use = '111' AND
            parcels.sale_price > 0 AND
            parcels.date_sold BETWEEN %(begin_date)s AND %(end_date)s
        GROUP BY objectid
        ORDER BY mean_sale_price""",
        {'begin_date': begindate, 'end_date': enddate, 'table_name': AsIs('parcels_org_'+datadate)})

        rows = cur.fetchall()

        cur.execute("SET CLIENT_ENCODING TO UTF8")
        cur.execute("SET STANDARD_CONFORMING_STRINGS TO ON")
        cur.execute("BEGIN")

        for row in rows:
            cur.execute("INSERT INTO propsales_hds_"+datadate+" (objectid,mean_sale_price,min_sale_price,max_sale_price,median_sale_price,stddev_sale_price float8,total_sale_price,num_sales,begin_date,end_date) VALUES ('"+row[0]+"','"+str(row[1])+"','"+str(row[2])+"','"+str(row[3])+"','"+str(row[4])+"','"+str(row[5])+"','"+str(row[6])+"','"+str(row[7])+"','"+begindate+"','"+enddate+"')")

        cur.execute("COMMIT")
        cur.execute("ANALYZE %(table_name)s",{'table_name': AsIs('propsales_hds_'+datadate)})

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Runs the programs.
createpropsale("100517")
#insertpropsale('20161001','20170930','100517')
#insertpropsale('20151001','20160930','100517')
insertpropsale('20130101','20141231','100517')
