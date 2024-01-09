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

def lines_from_string(text:str, delimeter:str="\n") -> list[str]:
    """
    Gets a list of strings that represent the lines of the inputted string. 
    Lines are determined by line breaks, or an optional 'delimeter' parameter.
    
    Returns: 
        - list[str]
    """
    return text.split(delimeter)
    
