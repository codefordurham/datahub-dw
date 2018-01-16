import psycopg2, sys
from psycopg2.extensions import AsIs
import pandas as pd
import numpy as np

def extractsingfamhouse(datadate,featuretype):
    # Extracts property sale data from singfamhouse_'mmddyy' table and save the data to a csv file.
    columns = ['mean_sfno','tot_sfno','num_sfno','mean_sfoo','tot_sfoo','num_sfoo','prc_sfno']
    singfamhousing = pd.DataFrame(columns=columns)

    if featuretype == 'bgs':
       f = open('geoid10.csv','r')
       featureids = f.readlines()
       f.close()

       fid = 'geoid10'
    elif featuretype == 'hds':
       f = open('objectid.csv','r')
       featureids = f.readlines()
       f.close()

       fid = 'objectid'
    else:
        sys.exit('Incorrect feature type')


    conn = None
    try:
        conn = psycopg2.connect("dbname='durham_prop' user='jmcmanus' password='bulldurham'")
        cur = conn.cursor()
        cur.execute("""SELECT %(feature_id)s,
                          ROUND(mean_sfno_val::NUMERIC, 2),
                          ROUND(tot_sfno_val::NUMERIC, 2), num_sfno,
                          ROUND(mean_sfoo_val::NUMERIC, 2),
                          ROUND(tot_sfoo_val::NUMERIC, 2), num_sfoo
                       FROM %(table_name)s
                       ORDER BY %(feature_id)s""",
                       {'table_name': AsIs('singfamhouse_'+featuretype+'_'+datadate), 'feature_id': AsIs(fid)})

        rows = np.array(cur.fetchall())

        for featureid in featureids:
            index = np.where(rows[:,0] == featureid.strip())

            if index[0]:
                row = rows[index[0]][0]
                if row[3] != None:
                    if row[6] == None:
                        prc_sfno = '100.0'
                    elif row[6] != None:
                        prc_sfno = round((float(row[3])/(float(row[6])+float(row[3])))*100.0,2)
                    singfamhouse = pd.DataFrame([[row[1],row[2],row[3],row[4],row[5],row[6],prc_sfno]],index=[row[0]],columns=columns)
                elif row[3] == None:
                    prc_sfno = 'NaN'
                    singfamhouse = pd.DataFrame([['NaN','NaN','NaN',row[4],row[5],row[6],prc_sfno]],index=[row[0]],columns=columns)

                singfamhousing = singfamhousing.append(singfamhouse)
            else:
                singfamhouse = pd.DataFrame([['NaN','NaN','NaN','NaN','NaN','NaN','NaN']], index=[featureid.strip()], columns=columns)
                singfamhousing = singfamhousing.append(singfamhouse)

        return(singfamhousing)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

f = open('singfamhouse_hds_100517.csv','w')
f.write(pd.DataFrame(extractsingfamhouse('100517','hds')).to_csv(index_label='id'))
#f = open('singfamhouse_bgs_100517.csv','w')
#f.write(pd.DataFrame(extractsingfamhouse('100517','bgs')).to_csv(index_label='id'))
f.close()
