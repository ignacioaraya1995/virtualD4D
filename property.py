class Property:
    """A class to represent a real estate property with detailed geolocation data."""
    def __init__(self, folio, street_address, city, state, zipcode):
        self.folio = folio
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.image_path = False
        self.ai_property_analysis = False

    def __repr__(self):
        return f"Property({self.street_address}, {self.city}, {self.state}, {self.zipcode})"

    def __str__(self):
        return (f"Address: {self.street_address}, {self.city}, {self.state}, {self.zipcode}\n"
                f"Latitude: {self.latitude}, Longitude: {self.longitude}\n"
                f"Northeast: {self.northeast}, Southwest: {self.southwest}")
