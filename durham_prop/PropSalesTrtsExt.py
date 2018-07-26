import psycopg2,sys
from psycopg2.extensions import AsIs
import pandas as pd
import numpy as np

def extractpropsales(datadate):
    # Extracts property sale data from propsales_'mmddyy' table and save the data to a csv file.
    if datadate == '2001':
        datename = '9800'
    elif datadate == '2010':
        datename = '0709'
    elif datadate == '100517':
        datename = '1314'
    elif datadate == '011818':
        datename = '1517'
    else:
        sys.exit('Incorrect datadate')

    columns = ["meansp"+datename,"minsp"+datename,"maxsp"+datename,"mediansp"+datename,"stddevsp"+datename,"totsp"+datename,"nums"+datename]
    geo_id = 'geoid10'
    tablename = 'propsales_trts_'+datadate

    propsales = pd.DataFrame(columns=columns)

    f = open(geo_id+'.csv','r')
    geoids = f.readlines()
    f.close()

    geotrts = []

    for geoid in geoids:
        geotrts.append(geoid.strip()[:len(geoid.strip())-1])

    geotrts = list(set(geotrts))
    geotrts.sort()

    conn = None
    try:
        conn = psycopg2.connect("dbname='durham_prop' user='jmcmanus' password='bulldurham'")
        cur = conn.cursor()
        cur.execute("""SELECT %(geoid)s AS trtid10,
                      ROUND(mean_sale_price::NUMERIC, 2) AS meansp,
                      ROUND(min_sale_price::NUMERIC, 2) AS minsp,
                      ROUND(max_sale_price::NUMERIC, 2) AS maxsp,
                      ROUND(median_sale_price::NUMERIC, 2) AS mediansp,
                      ROUND(stddev_sale_price::NUMERIC, 2) AS stddevsp,
                      ROUND(total_sale_price::NUMERIC, 2) AS totsp, num_sales AS nums
                    FROM %(table_name)s
                    ORDER BY %(geoid)s""",
                    {'geoid': AsIs(geo_id), 'table_name': AsIs(tablename)})

        rows = np.array(cur.fetchall())

        for geotrt in geotrts:
            index = np.where(rows == geotrt)

            if index[0] >= 0:
                row = rows[index[0]][0]
                propsale = pd.DataFrame([[row[1],row[2],row[3],row[4],row[5],row[6],row[7]]],index=[row[0]],columns=columns)
                propsales = propsales.append(propsale)
            else:
                propsale = pd.DataFrame([['NaN','NaN','NaN','NaN','NaN','NaN','NaN']],index=[geotrt],columns=columns)
                propsales = propsales.append(propsale)

        return(propsales)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

f = open('propsalesltdb_9800_trts.csv','w')
f.write(pd.concat([extractpropsales('2001')], axis=1).to_csv(index_label='trtid10'))
f.close()
f = open('propsalesltdb_0709_trts.csv','w')
f.write(pd.concat([extractpropsales('2010')], axis=1).to_csv(index_label='trtid10'))
f.close()
f = open('propsalesltdb_1314_trts.csv','w')
f.write(pd.concat([extractpropsales('100517')], axis=1).to_csv(index_label='trtid10'))
f.close()
f = open('propsalesltdb_1517_trts.csv','w')
f.write(pd.concat([extractpropsales('011818')], axis=1).to_csv(index_label='trtid10'))
f.close()
