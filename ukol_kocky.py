import requests
import json

kocky = []

response = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=10')
data = response.json() 

for polozka in data:
    fakt = polozka['text']
    if fakt not in kocky:
        kocky.append(fakt)  

for fakt in kocky:
    index = kocky.index(fakt)
    kocky[index] = f"{index + 1}. {fakt}"

print(kocky)

with open('kocici_fakta.json', mode='w', encoding='utf-8') as output_file:
    json.dump(kocky, output_file, indent = 2)

