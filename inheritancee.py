class Samsung:
    manufacturer = "Samsung Inc."
    contactWebsite = "www.samsung.com/contact"

    def contact_details(self):
        print("To contact us , log on to ", self.contactWebsite)


class Tablet(Samsung):
    def __init__(self):
        self.year_of_manufacture = 2017

    def manufacture_details(self):
        print(f"This Macbook was manufactured in the year {self.year_of_manufacture} by {self.manufacturer}")


tablet = Tablet()
tablet.manufacture_details()
tablet .contact_details()
