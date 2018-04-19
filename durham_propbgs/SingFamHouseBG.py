import psycopg2,pdb
from psycopg2.extensions import AsIs

def createsingfamhouse(datadate,bgyr):
    #Define geoid
    if len(datadate) < 5:
        if datadate == '2001':
            if bgyr == 'bgs00':
                geo_id = 'geoid00'
                file_suffix = bgyr+'_'+datadate
            elif bgyr == 'bgs':
                geo_id = 'geoid10'
                file_suffix = bgyr+'_'+datadate
        else:
            geo_id = 'geoid10'
            file_suffix = bgyr+'_'+datadate
    else:
        geo_id = 'geoid10'
        file_suffix = bgyr+'_'+datadate

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
                          {'table_name': AsIs('singfamhouse_'+file_suffix), 'geoid': AsIs(geo_id)})
        cur.execute("""ALTER TABLE %(table_name)s ADD PRIMARY KEY (gid)""",
                   {'table_name': AsIs('singfamhouse_'+file_suffix)})

        cur.execute("""ALTER TABLE %(table_name)s
                       ADD CONSTRAINT %(table_name)s_uq
                       UNIQUE (%(geoid)s)""",
                       {'table_name': AsIs('singfamhouse_'+file_suffix), 'geoid': AsIs(geo_id)})
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insertsingfamhouse(datadate,bgyr):
    #Define geoid
    if len(datadate) < 5:
        tot_val = 'JMTCTM'
        land_use = 'akrdc1'
        site_addr = "akpst_ || ' ' || akpstn || ' ' || akpstp"
        own_addr = 'owadr1'
        if datadate == '2010':
            geo_id = 'geoid10'
            table_prefix = 'parcels_0101'
            feature_id = 'geoid10'
            file_suffix = bgyr+'_'+datadate
            cenbgyr = 'cenbg2010ft'
        elif datadate == '2001':
            if bgyr == 'bgs00':
                geo_id = 'geoid00'
                table_prefix = 'durhamparcelhistory'
                feature_id = 'bgroup'
                file_suffix = bgyr+'_'+datadate
                cenbgyr = 'cenbg2000ft'
            elif bgyr == 'bgs':
                geo_id = 'geoid10'
                table_prefix = 'durhamparcelhistory'
                feature_id = 'geoid10'
                file_suffix = bgyr+'_'+datadate
                cenbgyr = 'cenbg2010ft'
        else:
            geo_id = 'geoid10'
            table_prefix = 'parcels_0101'
            feature_id = 'geoid10'
            file_suffix = bgyr+'_'+datadate
            cenbgyr = 'cenbg2010ft'
    else:
        tot_val = 'total_valu'
        land_use = 'land_use'
        site_addr = 'site_addre'
        own_addr = 'owner_addr'
        feature_id = 'geoid10'
        geo_id = 'geoid10'
        table_prefix = 'parcels_org_'
        file_suffix = bgyr+'_'+datadate
        cenbgyr = 'cenbg2010ft'

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
            bgs.%(featureid)s AS geoid,
            SUM(parcels.%(totval)s) / COUNT(parcels.%(totval)s) AS mean_sfno_val,
            SUM(parcels.%(totval)s) AS tot_sfno_val,
            COUNT(parcels.%(totval)s) AS num_sfno
        FROM %(cen_bgyr)s AS bgs
        JOIN %(table_name)s AS parcels
        ON ST_Within(parcels.geom, bgs.geom)
        WHERE
            parcels.%(landuse)s = '111' AND
            bgs.%(featureid)s LIKE '37063%%' AND
            ARRAY_LENGTH(ARRAY_INTERSECT(STRING_TO_ARRAY(%(siteaddr)s,' '),
                                         STRING_TO_ARRAY(%(ownaddr)s,' ')),1) <= 1
        GROUP BY bgs.%(featureid)s
        ORDER BY mean_sfno_val""",
        {'table_name': AsIs(table_prefix+datadate), 'landuse': AsIs(land_use), 'totval': AsIs(tot_val), 'siteaddr': AsIs(site_addr), 'ownaddr': AsIs(own_addr), 'featureid': AsIs(feature_id), 'cen_bgyr': AsIs(cenbgyr)})

        rows = cur.fetchall()

        cur.execute("SET CLIENT_ENCODING TO UTF8")
        cur.execute("SET STANDARD_CONFORMING_STRINGS TO ON")
        cur.execute("BEGIN")

        #Insert single family non-owner occupied housing data
        for row in rows:
            cur.execute("INSERT INTO singfamhouse_"+file_suffix+
                        " ("+geo_id+",mean_sfno_val,tot_sfno_val,num_sfno) VALUES ('"+
                        row[0]+"','"+str(row[1])+"','"+str(row[2])+"','"+str(row[3])+"')")

        #Query for single family owner occupied housing data
        cur.execute("""SELECT
            bgs.%(featureid)s AS geoid,
            SUM(parcels.%(totval)s) / COUNT(parcels.%(totval)s) AS mean_sfoo_val,
            SUM(parcels.%(totval)s) AS tot_sfoo_val,
            COUNT(parcels.%(totval)s) AS num_sfoo
        FROM %(cen_bgyr)s AS bgs
        JOIN %(table_name)s AS parcels
        ON ST_Within(parcels.geom, bgs.geom)
        WHERE
            bgs.%(featureid)s LIKE '37063%%' AND
            parcels.%(landuse)s = '111' AND
            ARRAY_LENGTH(ARRAY_INTERSECT(STRING_TO_ARRAY(%(siteaddr)s,' '),
                                         STRING_TO_ARRAY(%(ownaddr)s,' ')),1) > 1
        GROUP BY bgs.%(featureid)s
        ORDER BY mean_sfoo_val""",
        {'table_name': AsIs(table_prefix+datadate), 'landuse': AsIs(land_use), 'totval': AsIs(tot_val), 'siteaddr': AsIs(site_addr), 'ownaddr':    AsIs(own_addr), 'featureid': AsIs(feature_id), 'cen_bgyr': AsIs(cenbgyr)})

        rows = cur.fetchall()

        #Insert single family owner occupied housing data
        for row in rows:
            cur.execute("INSERT INTO singfamhouse_"+file_suffix+
                        " ("+geo_id+",mean_sfoo_val,tot_sfoo_val,num_sfoo) VALUES ('"+
                        row[0]+"','"+str(row[1])+"','"+   str(row[2])+"','"+str(row[3])+"') "
                        "ON CONFLICT ("+geo_id+") DO UPDATE "
                        "SET mean_sfoo_val=EXCLUDED.mean_sfoo_val,tot_sfoo_val=EXCLUDED.tot_sfoo_val,"
                        "num_sfoo=EXCLUDED.num_sfoo")

        cur.execute("COMMIT")
        cur.execute("ANALYZE singfamhouse_"+file_suffix)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Runs the programs.
#createsingfamhouse("100517","bgs")
#insertsingfamhouse("100517","bgs")
#createsingfamhouse("011818","bgs")
#insertsingfamhouse("011818","bgs")
#createsingfamhouse("2001","bgs")
#insertsingfamhouse('2001',"bgs")
createsingfamhouse("2001","bgs00")
insertsingfamhouse('2001',"bgs00")
