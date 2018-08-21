import pandas as pd



def fetch_permit_data():
    LAST_RECORD = 5289328

    permitFetch = pd.read_json('http://gisweb2.durhamnc.gov/arcgis/rest/services/iMaps/AllPermits/MapServer/0/query?where=1%3D1&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=4326&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&f=pjson', typ='series')['features']

    permits = [ { **permit['attributes'], 'geometry': permit['geometry'] } for permit in permitFetch]

    permitData = pd.DataFrame(permits)

    most_recent_record = permitFetch[-1]['attributes']['OBJECTID']
    
    while most_recent_record < LAST_RECORD:
        permitFetch = pd.read_json(f'http://gisweb2.durhamnc.gov/arcgis/rest/services/iMaps/AllPermits/MapServer/0/query?where=OBJECTID%3E{most_recent_record}&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=4326&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&f=pjson', typ='series')['features']
        permits = [ { **permit['attributes'], 'geometry': permit['geometry'] } for permit in permitFetch]
        permitData = permitData.append(pd.DataFrame(permits))
        most_recent_record = permitFetch[-1]['attributes']['OBJECTID']

    permitData.to_csv('durham_bldgpermits')

if __name__ == "__main__":
    fetch_permit_data()


