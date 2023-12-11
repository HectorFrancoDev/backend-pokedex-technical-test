class Pokemon:
    # El constructor
    def __init__(self, id, name, types, abilities, sprites):
        """Initialize the Pokemon class with the given parameters

        Args:
            id (number): ID of the Pokemon and Pokedex number
            name (string): Name of the Pokemon
            types (list): List all the types of the Pokemon
            abilities (list): List the abilities of the Pokemon
            sprites (list): List the available sprites (pics) of the Pokemon
        """
        self.id = id
        self.name = name
        self.types = types
        self.abilities = abilities
        self.sprites = sprites

    # Devuelve los datos del Pokémon en formato JSON
    def to_json(self) -> dict:
        """Returns the Pokemon object as JSON format

        Returns:
            JSON: Pokemon
        """
        return {
            "id": self.id,
            "name": self.name,
            "types": self.types,
            "abilities": self.abilities,
            "sprites": self.sprites,
        }
