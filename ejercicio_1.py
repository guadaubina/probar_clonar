class Persona:
    def __init__(self, energia):
        self.energia = energia
        self.es_feliz = False

    def energia_actual(self):
        return self.energia

    def comer (self):
        if (self.energia + 15) <= 100:
            self.energia += 15
        else:
            self.energia = 100