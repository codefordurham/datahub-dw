import psycopg2,sys,pdb
from psycopg2.extensions import AsIs
import pandas as pd
import numpy as np

def extractpropsales(begin_year):
    # Extracts property sale data from propsales_'mmddyy' table and save the data to a csv file.
    if begin_year == '1998':
        columns = ["meansp9800","minsp9800","maxsp9800","mediansp9800","stddevsp9800","totsp9800","nums9800","mhi99","pir9800","mgr_phi99","mmoc_phi99"]
        geo_id = 'geoid00'
        tablename = 'propsalesdec_2000_bgs'
    elif begin_year == '2013':
        columns = ["meansp1314","minsp1314","maxsp1314","mediansp1314","stddevsp1314","totsp1314","nums1314","mhi1314","pir1314"]
        geo_id = 'geoid10'
        tablename = 'propsalescompass_1314_bgs'
    elif begin_year == '2015':
        columns = ["meansp1517","minsp1517","maxsp1517","mediansp1517","stddevsp1517","totsp1517","nums1517","mhi16","pir1517","mgr_phi16","mmoc_phi16"]
        geo_id = 'geoid10'
        tablename = 'propsalesacs_2016_bgs'
    else:
        sys.exit('Incorrect Begin Year!')

    propsales = pd.DataFrame(columns=columns)

    f = open(geo_id+'.csv','r')
    geoids = f.readlines()
    f.close()

    conn = None
    try:
        conn = psycopg2.connect("dbname='durham_prop' user='jmcmanus' password='bulldurham'")
        cur = conn.cursor()
        if begin_year == '2013':
            cur.execute("""SELECT %(geoid)s,
                          ROUND(mean_sale_price::NUMERIC, 2) AS meansp,
                          ROUND(min_sale_price::NUMERIC, 2) AS minsp,
                          ROUND(max_sale_price::NUMERIC, 2) AS maxsp,
                          ROUND(median_sale_price::NUMERIC, 2) AS mediansp,
                          ROUND(stddev_sale_price::NUMERIC, 2) AS stddevsp,
                          ROUND(total_sale_price::NUMERIC, 2) AS totsp, num_sales AS nums,
                          ROUND(mhi::NUMERIC, 2) AS mhi, ROUND(pir::NUMERIC, 2) AS pir
                       FROM %(table_name)s
                       WHERE EXTRACT(YEAR FROM begin_date) = %(year)s
                       ORDER BY %(geoid)s""",
                       {'geoid': AsIs(geo_id), 'year': begin_year, 'table_name': AsIs(tablename)})

        else:
            cur.execute("""SELECT %(geoid)s,
                          ROUND(mean_sale_price::NUMERIC, 2) AS meansp,
                          ROUND(min_sale_price::NUMERIC, 2) AS minsp,
                          ROUND(max_sale_price::NUMERIC, 2) AS maxsp,
                          ROUND(median_sale_price::NUMERIC, 2) AS mediansp,
                          ROUND(stddev_sale_price::NUMERIC, 2) AS stddevsp,
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
                if begin_year == '2013':
                    propsale = pd.DataFrame([[row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]]], index=[row[0]], columns=columns)

                else:
                    propsale = pd.DataFrame([[row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]]], index=[row[0]], columns=columns)

                propsales = propsales.append(propsale)
            else:
                if begin_year == '2013':
                    propsale = pd.DataFrame([['NaN','NaN','NaN','NaN','NaN','NaN','NaN','NaN','NaN']], index=[geoid.strip()], columns=columns)
                else:
                    propsale = pd.DataFrame([['NaN','NaN','NaN','NaN','NaN','NaN','NaN','NaN','NaN','NaN','NaN']], index=[geoid.strip()], columns=columns)

                propsales = propsales.append(propsale)

        return(propsales)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

f = open('propsalesacs_1517_bgs.csv','w')
f.write(pd.concat([extractpropsales('2015')], axis=1).to_csv(index_label='id'))
f.close()
f = open('propsalesdec_9800_bgs.csv','w')
f.write(pd.concat([extractpropsales('1998')], axis=1).to_csv(index_label='id'))
f.close()
f = open('propsalescompass_1314_bgs.csv','w')
f.write(pd.concat([extractpropsales('2013')], axis=1).to_csv(index_label='id'))
f.close()
