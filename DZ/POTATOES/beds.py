class Beds:

    def __init__(self, pts: list):
        self.list_potatoes = pts

    def grow(self):
        for i in self.list_potatoes:
            i.grow()

    def speak(self):
        for i in self.list_potatoes:
            i.speak()