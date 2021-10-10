import pandas as pd
import pathlib

localpath = str(pathlib.Path(__file__).parent.resolve())
markers ={
    'ores': 'ore'
}

j = pd.read_json(fr'{localpath}\{markers["ores"]}_markers.json')
j = dict(j["ores"]["iron"])
empty = []
for k in j:
    splitterx = str(j[k]["x"]).split(".", 1)[0]
    splittery = str(j[k]["y"]).split(".", 1)[0]
    empty.append([splitterx, splittery])
print(empty)
