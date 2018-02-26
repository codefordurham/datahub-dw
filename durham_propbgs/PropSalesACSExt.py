import psycopg2, sys
from psycopg2.extensions import AsIs
import pandas as pd
import numpy as np

def extractpropsalescompass(begin_year):
    # Extracts property sale data from propsales_'mmddyy' table and save the data to a csv file.
    # columns = ["msp"+begin_year,"tsp"+begin_year,"ns"+begin_year]
    columns = ["meansp","minsp","maxsp","mediansp","totsp","nums","mhi","pir","mgr_phi","mmoc_phi"]
    propsales = pd.DataFrame(columns=columns)

    if begin_year == '1998':
        geo_id = 'geoid00'
        tablename = 'propsalesacs_2000_bgs'
    elif begin_year == '2015':
        geo_id = 'geoid10'
        tablename = 'propsalesacs_2016_bgs'
    else:
        sys.exit('Incorrect Begin Year!')

    f = open(geo_id+'.csv','r')
    geoids = f.readlines()
    f.close()

    conn = None
    try:
        conn = psycopg2.connect("dbname='durham_prop' user='jmcmanus' password='bulldurham'")
        cur = conn.cursor()
        cur.execute("""SELECT %(geoid)s,
                          ROUND(mean_sale_price::NUMERIC, 2) AS meansp,
                          ROUND(min_sale_price::NUMERIC, 2) AS minsp,
                          ROUND(max_sale_price::NUMERIC, 2) AS maxsp,
                          ROUND(median_sale_price::NUMERIC, 2) AS mediansp,
                          ROUND(total_sale_price::NUMERIC, 2) AS totsp, num_sales AS nums,
                          ROUND(mhi::NUMERIC, 2) AS mhi, ROUND(pir::NUMERIC, 2) AS pir,
                          ROUND(mgr_phi::NUMERIC, 2) AS mgr_phi, ROUND(mmoc_phi::NUMERIC, 2) AS mmoc_phi
                       FROM %(table_name)s
                       WHERE EXTRACT(YEAR FROM begin_date) = %(year)s
                       ORDER BY %(geoid)s""",
                       {'geoid': AsIs(geo_id), 'year': begin_year, 'table_name': AsIs(tablename)})

        rows = np.array(cur.fetchall())

        for geoid in geoids:
            index = np.where(rows == geoid.strip())

            if index[0]:
                row = rows[index[0]][0]
                propsale = pd.DataFrame([[row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]]], index=[row[0]], columns=columns)
                propsales = propsales.append(propsale)
            else:
                propsale = pd.DataFrame([['NaN','NaN','NaN','NaN','NaN','NaN','NaN','NaN','NaN','NaN']], index=[geoid.strip()], columns=columns)
                propsales = propsales.append(propsale)

        return(propsales)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

f = open('propsalesacs_2017_bgs.csv','w')
f.write(pd.concat([extractpropsalescompass('2015')], axis=1).to_csv(index_label='id'))
f.close()
