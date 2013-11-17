import pymongo as mongodb
from bson.objectid import ObjectId
class LocationDAO:
    
    def __init__(self):
        self.client = mongodb.MongoClient('mongodb://localhost:27017')
        self.locations=self.client.db.locations
        
    def findAll(self):
        return self.locations.find()
    
    def findByName(self, name):
        return self.locations.find({"Name": { "$regex": '(.)*'+name+'(.)*', "$options":'i'}})
    
    def findById(self,id):
        return self.locations.find_one({"_id": ObjectId(id)})
    
    def create(self,location):
        id = self.locations.insert({
                                      "Name" : location.name,
                                      "City" : location.city,
                                      "Country" : location.country,
                                      "Lat" : location.lat,
                                      "Long" : location.long,
                                      "PhotoURL" : location.photo_url
                                      })
        location.id=id
              
    def update(self,location):
        res = self.locations.save({   "_id" : ObjectId(location.id),
                                      "Name" : location.name,
                                      "City" : location.city,
                                      "Country" : location.country,
                                      "Lat" : location.lat,
                                      "Long" : location.long,
                                      "PhotoURL" : location.photo_url
                                      })
        if res:
            print "UPDATE successful"
        else:
            print "UPDATE failed"
    def delete(self,location):
        return self.locations.remove({"_id": location.id})