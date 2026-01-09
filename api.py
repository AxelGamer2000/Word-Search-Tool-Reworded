import re, json, pathlib
from enum import Enum

settingsFile = pathlib.Path("settings.json")

def replace(target, repl, string) -> str:
    string = re.sub(rf"\b{target}\b", repl, string)
    return string

def remove(target, string) -> str:
    string = replace(target, "", string)
    return string

def search(target, string) -> str:
    string = replace(target, f"**{target}**", string)
    return string

def replaceAll(targets:list, repls:list, string:str) -> str:
    limit = min(len(targets), len(repls))
    for i in range(limit):
        target = targets[i]
        repl = repls[i]
        string = replace(target, repl, string)
    return string

def removeAll(targets:list, string:str) -> str:
    for i in range(len(targets)):
        target = targets[i]
        string = remove(target, string)
    return string

def searchAll(targets:list, string:str) -> str:
    for i in range(len(targets)):
        target = targets[i]
        string = search(target, string)
    return string

def getSettingsKey(key: str):
    data = json.loads(settingsFile.read_text("utf-8"))
    return data[key]

def applySettingsChange(content: dict):
    settingsFile.write_text(json.dumps(content, indent=2))

def getSettingsKeyOrDefault(key: str, default):
    data = json.loads(settingsFile.read_text("utf-8"))

    if key in data:
        return data[key]
    else:
        return default

def getEnumFromValue(enum: Enum, value: str):
    for key in enum:
        if key == value:
            return key
    return None