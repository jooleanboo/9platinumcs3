class StringInstrument:
    def __init__(self, instrument_name, instrument_type, number_of_strings, is_tuned):
        self.instrument_name = instrument_name
        self.instrument_type = instrument_type
        self.number_of_strings = number_of_strings
        self.__is_tuned = is_tuned

    def tune(self):
        self.__is_tuned = True
        print(f"{self.instrument_name} has been tuned.")

    def play_string(self, string_number):
        if 1 <= string_number <= self.number_of_strings:
            print(f"Playing string {string_number} of {self.instrument_name}.")
        else:
            print(f"String {string_number} does not exist.")

    def get_tuning_status(self):
        return self.__is_tuned

    def display_info(self):
        print(f"Instrument Name: {self.instrument_name}")
        print(f"Instrument Type: {self.instrument_type}")
        print(f"Number of Strings: {self.number_of_strings}")
        print(f"Is Tuned: {self.__is_tuned}")


class Guitarist:
    def __init__(self, name, favorite_genre):
        self.name = name
        self.favorite_genre = favorite_genre
        self.__instruments = []

    def add_instrument(self, instrument):
        self.__instruments.append(instrument)

    def display_instruments(self):
        print(f"{self.name}'s guitars:")
        for instrument in self.__instruments:
            print(
                f"- {instrument.instrument_name}: "
                f"{instrument.instrument_type}, "
                f"{instrument.number_of_strings} strings"
            )

    def get_instruments(self):
        return self.__instruments


bonaobra = Guitarist("Bonaobra", "Alternative")

julian = StringInstrument("Julian", "Acoustic Guitar", 6, True)
xander = StringInstrument("Xander", "Electric Guitar", 6, False)
joolean = StringInstrument("Joolean", "Classical Guitar", 6, True)

print("--- BEFORE RELATIONSHIP ---")
print(f"Guitarist: {bonaobra.name}")
print(f"Favorite Genre: {bonaobra.favorite_genre}")
print(f"Number of guitars: {len(bonaobra.get_instruments())}")

print("\nThe guitars have been created:")
julian.display_info()
print()
xander.display_info()
print()
joolean.display_info()

print("\n--- BUILDING RELATIONSHIP ---")
print("Adding guitars to Bonaobra's collection...")

bonaobra.add_instrument(julian)
bonaobra.add_instrument(xander)
bonaobra.add_instrument(joolean)

print("\n--- AFTER RELATIONSHIP ---")
print(f"{bonaobra.name} has {len(bonaobra.get_instruments())} guitars.")

print("\nRelated guitars:")
bonaobra.display_instruments()

print("\n--- ACCESSING DATA THROUGH THE RELATIONSHIP ---")

for guitar in bonaobra.get_instruments():
    print(
        f"{guitar.instrument_name} is a "
        f"{guitar.instrument_type} with "
        f"{guitar.number_of_strings} strings."
    )
