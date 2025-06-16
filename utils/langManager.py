import json
from utils import helpers


def loadJsonFile(filename):
    with open(helpers.resource_path(filename), encoding = 'utf8') as file:
        return json.load(file)
    
def getLangContent(lang):
    if lang == 'ar':
        data = loadJsonFile('lang/ar.json')
        for key in data:
            if isinstance(data[key], str):
                data[key] = helpers.makeArabic(data[key])
        return data
    else:
        return loadJsonFile('lang/en.json')
