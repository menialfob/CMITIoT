import pymongo

def Directionsupload(id,x,y)    
    conn = pymongo.MongoClient("mongodb://menialfob:kultM8urhiB@ds055935.mongolab.com:55935/cmitiot")
    db = conn.cmitiot
    collection = db.roskildedirections

    data = {}
    data['ID'] = id
    data['Xcoor'] = x
    data['Ycoor'] = y
