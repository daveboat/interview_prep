class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @property
    def car_name(self):
        return "{} {} {}".format(self.year, self.make, self.model)

    @property
    def car_name_no_year(self):
        return "{} {}".format(self.make, self.model)
