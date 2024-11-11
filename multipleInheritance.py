class OperatingSystem:
    multitasking = True
    name = "sam"


class Samsung:
    website = "www.samsung.com"
    name = "sung"


class Tablet(OperatingSystem, Samsung):
    def __init__(self):
        if self.multitasking is True:
            print("This is a multitasking system")
            print("Name :", self.name)


tablet = Tablet()
