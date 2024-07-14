import json
import os

listOfFiles = os.listdir("indented_data")

for i in listOfFiles:
    with open(f"indented_data/{i}") as f:
        data = json.load(f)
        with open(f"data/{i}", "w") as wf:
            json.dump(data, wf)

