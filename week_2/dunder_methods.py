class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
    
    def __repr__(self):
        return f"Latitude = {self.latitude}, Longitude= {self.longitude}"
    
    def __str__(self):
        return f"{self.latitude}, {self.longitude}"

academy = Location(52.488, -1.88)

print(academy.__repr__())
    