class Gardener:
    def __init__(self, name: str):
        self.name = name
        
    def harvest(self, beds_list):
        for bed in beds_list:
            for potato in bed.list_potatoes:
                if potato._age == 3:
                    print(f"{self.name} собрал картошку {potato.number}")
                    potato._age = 0  