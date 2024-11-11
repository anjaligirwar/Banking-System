class MusicalInstruments:
    number_of_major_keys = 12


class StringInstruments(MusicalInstruments):
    type_of_wood = "Tonewood"


class Guitar(StringInstruments):
    def __init__(self):
        self.number_of_strings = 6
        print(f"This guitar consists of {self.number_of_strings} strings. It is made of {self.type_of_wood} "
              f"and it can play {self.number_of_major_keys} key ")


guitar = Guitar()
