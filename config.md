# Configuration Options For CloveShuffler
This is the configration documentation for CloveShuffler. All aspects of the config.json file will be displayed here.
# Variables
* [autoshuffle](#autoshuffle)
* [autoshuffle_method](#autoshuffle_method)
## autoshuffle
A boolean type that determines whether to automatically run the autoshuffle_method every time a card is answered.

Default: false
## autoshuffle_method
An integer type that determines what cards should be shuffled when autoshuffle is enabled.

Default: 0
### Values
* 0: Shuffle only cards tagged with "shuffle" that are in the current deck
* 1: Shuffle every tagged card in every deck
* 2: Shuffle only cards within the current deck
* 3: Shuffle all cards in every deck