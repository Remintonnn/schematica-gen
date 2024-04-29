import json

def getSettings() -> dict:
    settings = {}
    with open('settings.json') as f:
        settings = json.load(f)
    return settings
    
def saveSettings():
    pass