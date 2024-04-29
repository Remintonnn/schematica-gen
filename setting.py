import json
import regex

def getSettings() -> dict:
    settings = {}
    with open('settings.json') as f:
        settings = json.load(f)
    return settings
    
def saveSettings(settings:dict) -> None:
    with open('settings.json','w') as f:
        s = json.dumps(settings, indent=4)
        s = regex.sub('(\s*){\s*"id": ("[a-zA-Z_]+"),\s*"block": ("[a-zA-Z_]+")\s*}(,?\s*)', r'\1{"id":\2,"block":\3}\4', s)
        f.write(s)