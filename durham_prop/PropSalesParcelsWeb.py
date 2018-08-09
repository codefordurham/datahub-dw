import requests, json
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def extractpropsales(featuretype, begindate, enddate):
    parcels = pd.read_csv('propsaleparcels'+featuretype+begindate+'-'+enddate+'.csv',sep='|',index_col='parcelid')
    parcels.index = parcels.index.map(str)
    dictparcels = parcels.to_dict(orient='index')

    for k, v in dictparcels.items():
        parcelid = str(k)
        url = 'https://property.spatialest.com/nc/durham/property/'+parcelid+'/sales'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        if page.status_code == 200:
            table = soup.find_all('table', class_='table table-striped table-bordered')[0]
            saledates = []
            saleprices = []

            for row in table.find_all('tr'):
                columns = row.find_all('td')
                if len(columns) == 2:
                    if columns[0].get_text():
                        d = datetime.strptime(columns[0].get_text(), '%b-%d-%Y')
                        saledate = d.strftime('%Y%m%d')
                        saledates.append(saledate)
                        saleprices.append(int("".join(columns[1].get_text()[1:].split(","))))

            v.update({'saledates': saledates})
            v.update({'saleprices': saleprices})

        else:
            print(page.status_code)

    jsonparcels = json.dumps(dictparcels, indent=1)
    f = open('propsalesparcels'+featuretype+begindate+'-'+enddate+'.json','w')
    f.write(jsonparcels)
    f.close()

#extractpropsales('bgs','20150101','20171231')
#extractpropsales('bgs','20130101','20141231')
#extractpropsales('bgs','20080101','20091231')
#extractpropsales('bgs','19980101','20001231')
extractpropsales('bgs00','19980101','20001231')
