import psycopg2,sys
import pandas as pd
import numpy as np

def extractmissingmiddle(datadate,unittype):
    if datadate == "011818":
        if unittype == "singlefamily":
            columns = ["singlefamily_2018"]
            sqlcommand = """SELECT COUNT(land_use)
                               FROM parcels_org_011818
                               WHERE land_use = '111'"""
        elif unittype == "two2four":
            columns = ["two2four_2018"]
            sqlcommand = """SELECT COUNT(land_use)
                               FROM parcels_org_011818
                               WHERE land_use BETWEEN '112' AND '114'"""
        elif unittype == "townhouse":
            columns = ["townhouse_2018"]
            sqlcommand = """SELECT COUNT(land_use)
                               FROM parcels_org_011818
                               WHERE land_use = '122'"""
        elif unittype == "condo":
            columns = ["condo_2018"]
            sqlcommand = """SELECT COUNT(land_use)
                               FROM parcels_org_011818
                               WHERE land_use BETWEEN '120' AND '121'"""
        elif unittype == "multidwg":
            columns = ["multidwg_2018"]
            sqlcommand = """SELECT COUNT(land_use)
                               FROM parcels_org_011818
                               WHERE land_use = '180'"""
        elif unittype == "aprtmt":
            columns = ["aprtmt_2018"]
            sqlcommand = """SELECT COUNT(land_use)
                               FROM parcels_org_011818
                               WHERE land_use BETWEEN '410' AND '413'"""
        elif unittype == "vacant":
            columns = ["vacant_2018"]
            sqlcommand = """SELECT COUNT(land_use)
                               FROM parcels_org_011818
                               WHERE land_use BETWEEN '310' AND '319'"""
        else:
            sys.exit("Incorrect unittype")
    elif datadate == "2001":
        if unittype == "singlefamily":
            columns = ["singlefamily_2000"]
            sqlcommand = """SELECT COUNT(akrdc1)
                               FROM durhamparcelhistory2001
                               WHERE akrdc1 = '111'"""
        elif unittype == "two2four":
            columns = ["two2four_2000"]
            sqlcommand = """SELECT COUNT(akrdc1)
                               FROM durhamparcelhistory2001
                               WHERE akrdc1 BETWEEN '112' AND '114'"""
        elif unittype == "townhouse":
            columns = ["townhouse_2000"]
            sqlcommand = """SELECT COUNT(akrdc1)
                               FROM durhamparcelhistory2001
                               WHERE akrdc1 = '122'"""
        elif unittype == "condo":
            columns = ["condo_2000"]
            sqlcommand = """SELECT COUNT(akrdc1)
                               FROM durhamparcelhistory2001
                               WHERE akrdc1 BETWEEN '120' AND '121'"""
        elif unittype == "multidwg":
            columns = ["multidwg_2000"]
            sqlcommand = """SELECT COUNT(akrdc1)
                               FROM durhamparcelhistory2001
                               WHERE akrdc1 = '180'"""
        elif unittype == "aprtmt":
            columns = ["aprtmt_2000"]
            sqlcommand = """SELECT COUNT(akrdc1)
                               FROM durhamparcelhistory2001
                               WHERE akrdc1 BETWEEN '410' AND '413'"""
        elif unittype == "vacant":
            columns = ["vacant_2000"]
            sqlcommand = """SELECT COUNT(akrdc1)
                               FROM durhamparcelhistory2001
                               WHERE akrdc1 BETWEEN '310' AND '319'"""
        else:
           sys.exit("Incorrect unittype")
    else:
        sys.exit("Incorrect datadate")

    conn = None

    try:
        conn = psycopg2.connect("dbname='durham_prop' user='jmcmanus' password='bulldurham'")
        cur = conn.cursor()

        cur.execute(sqlcommand)

        rows = np.array(cur.fetchall())
        data = pd.DataFrame(rows, columns=columns)

        return(data)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

