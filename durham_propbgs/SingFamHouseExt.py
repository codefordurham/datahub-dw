import psycopg2
from psycopg2.extensions import AsIs
import pandas as pd
import numpy as np

def extractsingfamhouse(datadate):
    # Extracts property sale data from singfamhouse_'mmddyy' table and save the data to a csv file.
    columns = ['mean_sfno','tot_sfno','num_sfno','mean_sfoo','tot_sfoo','num_sfoo','prc_sfno']
    singfamhousing = pd.DataFrame(columns=columns)

    f = open('data/geoid10.csv','r')
    geoids = f.readlines()
    f.close()

    conn = None
    try:
        conn = psycopg2.connect("dbname='durham_prop' user='jmcmanus' password='bulldurham'")
        cur = conn.cursor()
        cur.execute("""SELECT geoid10,
                          ROUND(mean_sfno_val::NUMERIC, 2),
                          ROUND(tot_sfno_val::NUMERIC, 2), num_sfno,
                          ROUND(mean_sfoo_val::NUMERIC, 2),
                          ROUND(tot_sfoo_val::NUMERIC, 2), num_sfoo
                       FROM %(table_name)s
                       ORDER BY geoid10""",
                       {'table_name': AsIs('singfamhouse_'+datadate)})

        rows = np.array(cur.fetchall())

        for geoid in geoids:
            index = np.where(rows == geoid.strip())

            if index[0]:
                row = rows[index[0]][0]
                if row[3] != None:
                    prc_sfno = round((float(row[3])/(float(row[6])+float(row[3])))*100.0,2)
                    singfamhouse = pd.DataFrame([[row[1],row[2],row[3],row[4],row[5],row[6],prc_sfno]],index=[row[0]],columns=columns)
                elif row[3] == None:
                    prc_sfno = 'NaN'
                    singfamhouse = pd.DataFrame([['NaN','NaN','NaN',row[4],row[5],row[6],prc_sfno]],index=[row[0]],columns=columns)

                singfamhousing = singfamhousing.append(singfamhouse)
            else:
                singfamhouse = pd.DataFrame([['NaN','NaN','NaN','NaN','NaN','NaN','NaN']], index=[geoid.strip()], columns=columns)
                singfamhousing = singfamhousing.append(singfamhouse)

        return(singfamhousing)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

f = open('singfamhouse_100517.csv','w')
f.write(pd.DataFrame(extractsingfamhouse('100517')).to_csv(index_label='id'))
f.close()
