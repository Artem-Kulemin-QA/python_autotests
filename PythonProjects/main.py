import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a0a1baed778c05085fa5b94f4bb7c235'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
 
body_fix = {
    "pokemon_id": "43507",
    "name": "Zohan",
    "photo_id": 2
}

body_pokebol = {
    "pokemon_id": "43507"
}
'''Создание покемона'''

'''response_create = requests.post(url = f'{URL}/pokemons',headers = HEADER,json = body_create)
print(response_create.text)'''

'''Смена имени покемона'''

'''response_fix = requests.put(url = f'{URL}/pokemons',headers = HEADER,json = body_fix)
print(response_fix.text)'''

'''Поймать покемона в покебол'''

response_pokebol = requests.post(url = f'{URL}/trainers/add_pokeball',headers = HEADER,json = body_pokebol)
print(response_pokebol.text)


          