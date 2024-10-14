class Location:
    lat: float
    lng: float

    def __init__(self, lat: float, lng: float):
        self.lat = lat
        self.lng = lng

    def print(self):
        print(f'<{self.lat}, {self.lng}>')

    @classmethod
    def parse(Location, s: str, /):
        lat, lng = s.split('/')
        lat = float(lat)
        lng = float(lng)

        return Location(
            lat=lat, 
            lng=lng
        )
