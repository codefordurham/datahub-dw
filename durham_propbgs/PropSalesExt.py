import psycopg2
from psycopg2.extensions import AsIs
import pandas as pd
import numpy as np

def extractpropsale(begin_year,datadate):
    # Extracts property sale data from propsales_'mmddyy' table and save the data to a csv file.
    columns = ["msp"+begin_year,"tsp"+begin_year,"ns"+begin_year]
    propsales = pd.DataFrame(columns=columns)

    f = open('data/geoid10.csv','r')
    geoids = f.readlines()
    f.close()

    conn = None
    try:
        conn = psycopg2.connect("dbname='durham_prop' user='jmcmanus' password='bulldurham'")
        cur = conn.cursor()
        cur.execute("""SELECT geoid10,
                          ROUND(mean_sale_price::NUMERIC, 2) AS msp,
                          ROUND(tot_sale_price::NUMERIC, 2) AS tsp, num_sales AS ns
                       FROM %(table_name)s
                       WHERE EXTRACT(YEAR FROM begin_date) = %(year)s
                       ORDER BY geoid10""",
                       {'year': begin_year, 'table_name': AsIs('propsales_'+datadate)})

        rows = np.array(cur.fetchall())

        for geoid in geoids:
            index = np.where(rows == geoid.strip())

            if index[0]:
                row = rows[index[0]][0]
                propsale = pd.DataFrame([[row[1],row[2],row[3]]], index=[row[0]], columns=columns)
                propsales = propsales.append(propsale)
            else:
                propsale = pd.DataFrame([['0.0','0.0','0.0']], index=[geoid.strip()], columns=columns)
                propsales = propsales.append(propsale)

        return(propsales)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

f = open('propsales_100517.csv','w')
f.write(pd.concat([extractpropsale('2015','100517'), extractpropsale('2016','100517')],axis=1).to_csv(index_label='GEOID10'))
f.close()
