import psycopg2
from psycopg2.extensions import AsIs

def createsingfamhouse(datadate):
    #Define geoid
    if len(datadate) < 5:
        if datadate == '2010':
            geo_id = 'geoid10'
        else:
            geo_id = 'geoid10'
    else:
        geo_id = 'geoid10'

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
                          mean_sfno_val float8,
                          tot_sfno_val float8,
                          num_sfno int,
                          mean_sfoo_val float8,
                          tot_sfoo_val float8,
                          num_sfoo int)""",
                          {'table_name': AsIs('singfamhouse_bgs_'+datadate), 'geoid': AsIs(geo_id)})
        cur.execute("""ALTER TABLE %(table_name)s ADD PRIMARY KEY (gid)""",
                   {'table_name': AsIs('singfamhouse_bgs_'+datadate)})

        cur.execute("""ALTER TABLE %(table_name)s
                       ADD CONSTRAINT %(table_name)s_uq
                       UNIQUE (%(geoid)s)""",
                       {'table_name': AsIs('singfamhouse_bgs_'+datadate), 'geoid': AsIs(geo_id)})
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insertsingfamhouse(datadate):
    #Define geoid
    if len(datadate) < 5:
        tot_val = 'JMTCTM'
        land_use = 'akrdc1'
        site_addr = "akpst_ || ' ' || akpstn || ' ' || akpstp"
        own_addr = 'owadr1'
        feature_id = 'geoid10'
        if datadate == '2010':
            geo_id = 'geoid10'
            table_prefix = 'parcels_0101'
        elif datadate == '2001':
            geo_id = 'geoid10'
            table_prefix = 'durhamparcelhistory'
        else:
            geo_id = 'geoid10'
            table_prefix = 'parcels_0101'
    else:
        tot_val = 'total_valu'
        land_use = 'land_use'
        site_addr = 'site_addre'
        own_addr = 'owner_addr'
        feature_id = 'geoid10'
        geo_id = 'geoid10'
        table_prefix = 'parcels_org_'

    # Aggrigates parcel propert sales to Census block-groups.
    conn = None
    try:
        conn = psycopg2.connect("dbname='durham_prop' user='jmcmanus' password='bulldurham'")
        cur = conn.cursor()

        #Create intersect function
        cur.execute("""CREATE OR REPLACE FUNCTION array_intersect(anyarray, anyarray)
                       RETURNS anyarray AS $$
                         SELECT ARRAY(SELECT unnest($1)
                                      INTERSECT
                                      SELECT unnest($2))
                       $$ LANGUAGE sql""")

        #Query for single family non-owner occupied housing data
        cur.execute("""SELECT
            bgs.%(geoid)s AS geoid,
            SUM(parcels.%(totval)s) / COUNT(parcels.%(totval)s) AS mean_sfno_val,
            SUM(parcels.%(totval)s) AS tot_sfno_val,
            COUNT(parcels.%(totval)s) AS num_sfno
        FROM cenbg2010 AS bgs
        JOIN %(table_name)s AS parcels
        ON ST_Within(parcels.geom, bgs.geom)
        WHERE
            bgs.countyfp10 = '063' AND
            parcels.%(landuse)s = '111' AND
            ARRAY_LENGTH(ARRAY_INTERSECT(STRING_TO_ARRAY(%(siteaddr)s,' '),
                                         STRING_TO_ARRAY(%(ownaddr)s,' ')),1) <= 1
        GROUP BY %(geoid)s
        ORDER BY mean_sfno_val""",
        {'table_name': AsIs(table_prefix+datadate), 'landuse': AsIs(land_use), 'totval': AsIs(tot_val), 'siteaddr': AsIs(site_addr), 'ownaddr': AsIs(own_addr), 'geoid': AsIs(feature_id)})

        rows = cur.fetchall()

        cur.execute("SET CLIENT_ENCODING TO UTF8")
        cur.execute("SET STANDARD_CONFORMING_STRINGS TO ON")
        cur.execute("BEGIN")

        #Insert single family non-owner occupied housing data
        for row in rows:
            cur.execute("INSERT INTO singfamhouse_bgs_"+datadate+
                        " ("+geo_id+",mean_sfno_val,tot_sfno_val,num_sfno) VALUES ('"+
                        row[0]+"','"+str(row[1])+"','"+str(row[2])+"','"+str(row[3])+"')")

        #Query for single family owner occupied housing data
        cur.execute("""SELECT
            bgs.%(geoid)s AS geoid,
            SUM(parcels.%(totval)s) / COUNT(parcels.%(totval)s) AS mean_sfoo_val,
            SUM(parcels.%(totval)s) AS tot_sfoo_val,
            COUNT(parcels.%(totval)s) AS num_sfoo
        FROM cenbg2010 AS bgs
        JOIN %(table_name)s AS parcels
        ON ST_Within(parcels.geom, bgs.geom)
        WHERE
            bgs.countyfp10 = '063' AND
            parcels.%(landuse)s = '111' AND
            ARRAY_LENGTH(ARRAY_INTERSECT(STRING_TO_ARRAY(%(siteaddr)s,' '),
                                         STRING_TO_ARRAY(%(ownaddr)s,' ')),1) > 1
        GROUP BY %(geoid)s
        ORDER BY mean_sfoo_val""",
        {'table_name': AsIs(table_prefix+datadate), 'landuse': AsIs(land_use), 'totval': AsIs(tot_val), 'siteaddr': AsIs(site_addr), 'ownaddr':    AsIs(own_addr), 'geoid': AsIs(feature_id)})

        rows = cur.fetchall()

        #Insert single family owner occupied housing data
        for row in rows:
            cur.execute("INSERT INTO singfamhouse_bgs_"+datadate+
                        " ("+geo_id+",mean_sfoo_val,tot_sfoo_val,num_sfoo) VALUES ('"+
                        row[0]+"','"+str(row[1])+"','"+   str(row[2])+"','"+str(row[3])+"') "
                        "ON CONFLICT ("+geo_id+") DO UPDATE "
                        "SET mean_sfoo_val=EXCLUDED.mean_sfoo_val,tot_sfoo_val=EXCLUDED.tot_sfoo_val,"
                        "num_sfoo=EXCLUDED.num_sfoo")

        cur.execute("COMMIT")
        cur.execute("ANALYZE singfamhouse_bgs_"+datadate)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Runs the programs.
#createsingfamhouse("100517")
#insertsingfamhouse('100517')
createsingfamhouse("011818")
insertsingfamhouse('011818')
#createsingfamhouse("2001")
#insertsingfamhouse('2001')
