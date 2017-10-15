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
                          geoid10 varchar(255),
                          mean_sale_price float8,
                          tot_sale_price float8,
                          num_sales int,
                          begin_date date,
                          end_date date)""",
                          {'table_name': AsIs('propsales_'+datadate)})
        cur.execute("""ALTER TABLE %(table_name)s ADD PRIMARY KEY (gid)""",
                   {'table_name': AsIs('propsales_'+datadate)})

        """for command in commands:
            cur.execute(command)"""

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
        cur.execute("""SELECT
            bgs.geoid10 AS geoid10,
            SUM(parcels.sale_price) / COUNT(parcels.sale_price) AS mean_sale_price,
            SUM(parcels.sale_price) AS tot_sale_price,
            COUNT(parcels.sale_price) AS num_sales
        FROM cenbg2010 AS bgs
        JOIN %(table_name)s AS parcels
        ON ST_Within(parcels.geom, bgs.geom)
        WHERE
            bgs.countyfp10 = '063' AND
            parcels.land_use = '111' AND
            parcels.sale_price > 0 AND
            parcels.date_sold BETWEEN %(begin_date)s AND %(end_date)s
        GROUP BY geoid10
        ORDER BY mean_sale_price""",
        {'begin_date': begindate, 'end_date': enddate, 'table_name': AsIs('parcels_org_'+datadate)})

        rows = cur.fetchall()

        cur.execute("SET CLIENT_ENCODING TO UTF8")
        cur.execute("SET STANDARD_CONFORMING_STRINGS TO ON")
        cur.execute("BEGIN")

        for row in rows:
            cur.execute("INSERT INTO propsales_"+datadate+" (geoid10,mean_sale_price,tot_sale_price,num_sales,begin_date,end_date) VALUES ('"+row[0]+"','"+str(row[1])+"','"+str(row[2])+"','"+str(row[3])+"','"+begindate+"','"+enddate+"')")

        cur.execute("COMMIT")
        cur.execute("ANALYZE propsales")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Runs the programs.
createpropsale("100517")
insertpropsale('20161001','20170930','100517')
insertpropsale('20151001','20170930','100517')
