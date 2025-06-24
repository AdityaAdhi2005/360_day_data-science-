class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"you are dirving {self.color} color {self.model}")
    def stop(self):
        print(f"you stoped {self.color} color {self.model}")
