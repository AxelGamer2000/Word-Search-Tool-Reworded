from magicgui import magicgui
from enum import Enum
import api, pathlib, darkdetect

api.settingsFile = pathlib.Path("../settings.json")

class Theme(str, Enum):
    AUTO = "auto"
    DARK = "dark"
    LIGHT = "light"

@magicgui(
    call_button="Apply"
)
def settings(
    title: str = api.getSettingsKeyOrDefault("title", "Word Search Tool: Reworded"),
):
    api.applySettingsChange(locals())

settings.show(run=True)