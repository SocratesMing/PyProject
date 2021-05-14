class Temperature:
    def __init__(self, temperature=0):

        self.temperature = temperature

    @property
    def fahrenheit(self):

        self.temperature = (self.temperature * 1.8) + 32

temp = Temperature(10)
temp.fahrenheit
print(temp.temperature)


class Temperature2:
    def __init__(self, temperature=0):

        self.temperature = temperature

    @property
    def fahrenheit(self):

        return (self.temperature * 1.8) + 32

temp = Temperature2(10)
temp.fahrenheit
print(temp.temperature)