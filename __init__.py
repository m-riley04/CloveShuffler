from aqt import mw
from aqt.utils import showInfo, qconnect, TextFormat
from aqt.qt import *
def isClove(text) -> bool:
    """
    Checks whether or not a card face has Clove text formatting.
    
    Returns: 
        - bool
    """
    if ("{{" in text & "}}" in text):
        return True
    return False

