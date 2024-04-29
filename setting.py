import json

def getSettings() -> dict:
    settings = {}
    with open('settings.json') as f:
        settings = json.load(f)
    return settings
    
def saveSettings(settings:dict) -> None:
    with open('settings.json','w') as f:
        f.write(json.dumps(settings))