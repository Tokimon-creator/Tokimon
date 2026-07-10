import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SAVE___FILE____ = os.path.join(BASE_DIR, "Tokimon_save.json")
def save_game(team, box, progress):
    data = {
    "team": team,
    "box": box,
    "progress": progress
    }
    with open(SAVE___FILE____, "w") as file:
        json.dump(data, file)
        
def load_game():
    with open(SAVE___FILE____, "r") as file:
        data = json.load(file)

    return data["team"], data["box"], data["progress"]     