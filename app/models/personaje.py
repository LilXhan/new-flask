class Personaje:
    def __init__(self, name, status, species, gender, img, location):
        self.name = name
        self.status = status
        self.species = species
        self.gender = gender
        self.img = img
        self.location = location
    
    def to_json(self):
        return {
            'name': self.name,
            'status': self.status,
            'species': self.species,
            'gender': self.gender,
            'img': self.img,
            'location': self.location
        }