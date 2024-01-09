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
    

def get_deck_cards(deckName:str) -> list[mw.Card]:
    """Returns a list of cards when given a deck's name"""
    # Form the search tag for cards without spaces
    searchTag = "deck:" + deckName
    searchTag = searchTag.replace(" ", "_")
    
    # Get a list of card IDs
    return mw.col.find_cards(searchTag)

