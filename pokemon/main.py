from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

# POKEMONS STORE MANAGEMENT WITH FAST API
# Create a fastAPI application for managing Pokemon data using Pydantic for validation and async programming for data handling.
# create a pydantic model for the pokemon data, add id and name

app = FastAPI()

class PokemonDetails(BaseModel):
    id: int
    name: str

class PokemonStore:
    stored_pokemon = {}


async def fetch_pokemon_data(pokemon_id: int):
    async with httpx.AsyncClient() as client:
        # Make an asynchronous request to the Pokémon API
        response = await client.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/")
        return response.json()

@app.get("/async_pokemon/{pokemon_id}", response_model=dict)
async def async_pokemon(pokemon_id: int):
    pokemon_data = await fetch_pokemon_data(pokemon_id)

    # Store Pokémon name and ID in the Pydantic BaseModel
    pokemon_details = PokemonDetails(id=pokemon_id, name=pokemon_data["name"])
    PokemonStore.stored_pokemon[pokemon_id] = pokemon_details

    return {"pokemon_data": pokemon_data, "stored_pokemon": PokemonStore.stored_pokemon}


@app.get("/pokemon_store", response_model=dict)
async def get_pokemon_store():
    return {"stored_pokemon": PokemonStore.stored_pokemon}