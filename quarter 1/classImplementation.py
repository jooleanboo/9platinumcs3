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


guitar = StringInstrument("Julian", "Acoustic Guitar", 6, False)
ukulele = StringInstrument("Xander", "Ukulele", 4, True)

print("--- BEFORE ---")
print("Object 1:")
guitar.display_info()

print("\nObject 2:")
ukulele.display_info()

print("\nPerforming action on Object 1...")
guitar.tune()

print("\n--- AFTER ---")
print("Object 1:")
guitar.display_info()

print("\nObject 2:")
ukulele.display_info()
