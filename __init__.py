from aqt import mw
from aqt.utils import showInfo, qconnect, TextFormat
from aqt.qt import *

def run():
    """
    The main command that is to be connected to the "Shuffle" action button. Does a sequence of actions:
    1. Accesses the current deck and cards
    2. Accesses the front and back fields of each cards
    3. Shuffles the accessed fields (if any Clove fields exist)
    
    Returns:
        - None
    """
    # Get a list of the current cards
    ids = get_current_cards()
    
    # Iterate through the card IDs
    for id in ids:
        # Initialize the card object
        card = mw.col.get_card(id)
        
        # Get the front and back text
        front = card.note().fields[0]
        back = card.note().fields[1]

        # Shuffle the card
        newFront = shuffle(front)
        
        # Show the user the shuffled card
        showInfo(newFront, None, None, "info", "Anki", "plain")
        
    # Tell the user the process is finished
    showInfo("Current deck's card answers have been successfully shuffled!")
            
def isClove(text) -> bool:
    """
    Checks whether or not a card face has Clove text formatting.
    
    Returns: 
        - bool
    """
    if ("{{" in text & "}}" in text):
        return True
    return False

def shuffle(text:str) -> str:
    """
    Shuffles the Clove answers of a card in a random order.
    
    Determines what lines to shuffle based on whether it finds Clove formatting in the line.
    If the first line does not have Clove formatting, it will stay the first line. After that,
    if any Clove lines are detected, the following lines will be shuffled with it. 
    
    Returns: 
        - str
    """
    # Break the text into lines
    frontLines = lines_from_string(text, "<br>")
    
    
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

def get_current_cards() -> list[mw.Card]:
    """
    Gets a list of the current deck's cards.
    
    Returns: 
        - list[Card]
    """
    # Get the current deck and name
    deck = mw.col.decks.current()
    deckName = deck.get("name")
    
    # Return the list of cards from helper function
    return get_deck_cards(deckName)

# Create the menu action for the plugin
action = QAction("Shuffle Answers", mw)
# Connect the signal of "triggered" to the "run" function
qconnect(action.triggered, run)
# Add the "Shuffle Answers" action to the tools dropdown menu
mw.form.menuTools.addAction(action)