import pandas as pd
import pathlib

localpath = str(pathlib.Path(__file__).parent.resolve())
markers ={
    'ores': 'ore',

}

essence_type = [
    'air_boid',
    'air_plant',
    'air_stone',
    'death_boid',
    'death_plant',
    'death_stone',
    'earth_boid',
    'earth_plant',
    'earth_stone',
    'fire_boid',
    'fire_plant',
    'fire_stone',
    'life_boid',
    'life_plant',
    'life_stone',
    'soul_boid',
    'soul_plant',
    'soul_stone',
    'water_boid',
    'water_plant',
    'water_stone']



c = pd.read_json(rf'{localpath}\chests.json')
j = pd.read_json(rf'{localpath}\essences.json')

chest_reg = c["chests"].keys()
list_dict = {}
for k in chest_reg:
    list_dict.update(dict(c["chests"][k]))
for e in essence_type:
    list_dict.update(dict(j["essences"][e]))
empty = []
for k in list_dict:
    splitterx = str(list_dict[k]["x"]).split(".", 1)[0]
    splittery = str(list_dict[k]["y"]).split(".", 1)[0]
    empty.append([splitterx, splittery])
print(empty)
