import psycopg2
from psycopg2.extensions import AsIs

def createsingfamhouse(datadate):
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
                          mean_sfno_val float8,
                          tot_sfno_val float8,
                          num_sfno int,
                          mean_sfoo_val float8,
                          tot_sfoo_val float8,
                          num_sfoo int)""",
                          {'table_name': AsIs('singfamhouse_hds_'+datadate)})
        cur.execute("""ALTER TABLE %(table_name)s ADD PRIMARY KEY (gid)""",
                   {'table_name': AsIs('singfamhouse_hds_'+datadate)})

        cur.execute("""ALTER TABLE %(table_name)s
                       ADD CONSTRAINT %(table_name)s_uq
                       UNIQUE (objectid)""",
                       {'table_name': AsIs('singfamhouse_hds_'+datadate)})
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insertsingfamhouse(datadate):
    # Aggrigates parcel propert sales to Census block-groups.
    conn = None
    try:
        conn = psycopg2.connect("dbname='durham_prop' user='jmcmanus' password='bulldurham'")
        cur = conn.cursor()

        #cur.execute(
        """CREATE OR REPLACE FUNCTION array_intersect(anyarray, anyarray)
                       RETURNS anyarray AS $$
                         SELECT ARRAY(SELECT unnest($1)
                                      INTERSECT
                                      SELECT unnest($2))
                       $$ LANGUAGE sql"""
        #)

        cur.execute("""SELECT
            hds.objectid AS objectid,
            SUM(parcels.total_valu) / COUNT(parcels.total_valu) AS mean_sfno_val,
            SUM(parcels.total_valu) AS tot_sfno_val,
            COUNT(parcels.total_valu) AS num_sfno
        FROM neighborhoods_ft AS hds
        JOIN %(table_name)s AS parcels
        ON ST_Within(parcels.geom, hds.geom)
        WHERE
            parcels.land_use = '111' AND
            ARRAY_LENGTH(ARRAY_INTERSECT(STRING_TO_ARRAY(site_addre,' '),
                                         STRING_TO_ARRAY(owner_addr,' ')),1) <= 1
        GROUP BY objectid
        ORDER BY mean_sfno_val""",
        {'table_name': AsIs('parcels_org_'+datadate)})

        rows = cur.fetchall()

        cur.execute("SET CLIENT_ENCODING TO UTF8")
        cur.execute("SET STANDARD_CONFORMING_STRINGS TO ON")
        cur.execute("BEGIN")

        for row in rows:
            cur.execute("INSERT INTO singfamhouse_hds_"+datadate+
                        " (objectid,mean_sfno_val,tot_sfno_val,num_sfno) VALUES ('"+
                        row[0]+"','"+str(row[1])+"','"+str(row[2])+"','"+str(row[3])+"')")

        cur.execute("""SELECT
            hds.objectid AS objectid,
            SUM(parcels.total_valu) / COUNT(parcels.total_valu) AS mean_sfoo_val,
            SUM(parcels.total_valu) AS tot_sfoo_val,
            COUNT(parcels.total_valu) AS num_sfoo
        FROM neighborhoods_ft AS hds
        JOIN %(table_name)s AS parcels
        ON ST_Within(parcels.geom, hds.geom)
        WHERE
            parcels.land_use = '111' AND
            ARRAY_LENGTH(ARRAY_INTERSECT(STRING_TO_ARRAY(site_addre,' '),
                                         STRING_TO_ARRAY(owner_addr,' ')),1) > 1
        GROUP BY objectid
        ORDER BY mean_sfoo_val""",
        {'table_name': AsIs('parcels_org_'+datadate)})

        rows = cur.fetchall()

        for row in rows:
            cur.execute("INSERT INTO singfamhouse_hds_"+datadate+
                        " (objectid,mean_sfoo_val,tot_sfoo_val,num_sfoo) VALUES ('"+
                        row[0]+"','"+str(row[1])+"','"+   str(row[2])+"','"+str(row[3])+"') "
                        "ON CONFLICT (objectid) DO UPDATE "
                        "SET mean_sfoo_val=EXCLUDED.mean_sfoo_val,tot_sfoo_val=EXCLUDED.tot_sfoo_val,"
                        "num_sfoo=EXCLUDED.num_sfoo")

        cur.execute("COMMIT")
        cur.execute("ANALYZE singfamhouse_hds_"+datadate)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Runs the programs.
createsingfamhouse("100517")
insertsingfamhouse('100517')
