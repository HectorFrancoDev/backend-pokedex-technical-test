import pytest

from pokemon import Pokemon, get_pokemon, get_all_pokemon


def test_get_pokemon():
    # Prueba que el método `get_pokemon()` devuelve los datos de un Pokémon
    p = get_pokemon(1)
    assert p.id == 1
    assert p.name == "Bulbasaur"