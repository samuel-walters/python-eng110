import requests

class Postcode:
    def __init__(self, results_dictionary):
        # country, region, admin_district, parish
        self.postcode = results_dictionary["postcode"]
        self.country = results_dictionary["country"]
        self.region = results_dictionary["region"]
        self.admin_district = results_dictionary["admin_district"]
        self.parish = results_dictionary["parish"]

