# La clase Pokemon
class Pokemon:
    # El constructor
    def __init__(self, id, name, types, abilities, sprites):
        self.id = id
        self.name = name
        self.types = types
        self.abilities = abilities
        self.sprites = sprites

    # Devuelve los datos del Pokémon en formato JSON
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "types": self.types,
            "abilities": self.abilities,
            "sprites": self.sprites,
        }
