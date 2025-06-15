class Potatoes:
    INFO_AGE = ("1", "2", "3", "4")

    def __init__(self, number: int):
        self.number = number
        self._age = 0

    def grow(self):
        if self._age != 3:
            self._age += 1
        else:
            print("РАСТИ")

    def speak(self):
        print(self._age)
        print(f"Картошка {self.number} сейчас {Potatoes.INFO_AGE[self._age]}")
