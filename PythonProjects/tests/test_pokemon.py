import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a0a1baed778c05085fa5b94f4bb7c235'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRENER_ID = '4345'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200



def test_part_response():
    response_get = requests.get(url = f'{URL}/trainers',params = {'trainer_id' : TRENER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'White Roger'




