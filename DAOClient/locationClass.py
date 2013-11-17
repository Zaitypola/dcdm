class Location:
    def __init__(self,name,city,country,latitude,longitude,photo_url):
        self.id=-1
        self.name=name
        self.city=city
        self.country=country
        self.lat=latitude
        self.long=longitude
        self.photo_url=photo_url       
    def toString(self):
        print "Name: " + self.name + " - City: " + self.city + " - Country: " + self.country + " - Longitude: " + str(self.long) + " - Latitude: " + str(self.lat) + " - Photo: " + self.photo_url
