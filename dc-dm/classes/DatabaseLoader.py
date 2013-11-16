from locationDAOClass import LocationsDAO
from locationClass import Location

def load_database():    
    client = LocationsDAO()
    print client.locations.count()
    for i in range(0,10):
        print "Location n:" + str(i)
        print "Insert attribute Name:"
        name = raw_input()
        print "Insert attribute Address:"
        address = raw_input()
        print "Insert attribute City:"
        city = raw_input()
        print "Insert attribute Country:"
        country = raw_input()
        print "Insert attribute Age:"
        age = raw_input()
        print "Insert attribute Theme:"
        theme = raw_input()
        print "Insert attribute Photo URL:"
        photo_url = raw_input()
        
        location = Location(name, address, city, country, age, theme, photo_url)
        client.create(location)
    
load_database()
