# CloveShuffler
CloveShuffler is an addon for Anki that can shuffle your Clove answers/lines in your flashcards. This is to stop you from simply memorizing the position or order of the answers.

# DISCLAIMER
This addon is in it's very early stages of development and release. It is entirely functional and usable in it's current state, however there are certain risks you take when using it. Nothing bad has happened yet in my testing, but you have been warned.

# Functionality
* Custom tag interfacing
* Manual Shuffling
    * Shuffle all cards in the current deck with the "shuffle" tag
    * Shuffle all cards with the "shuffle" tag
    * Shuffle all cards in the current deck
    * Shuffle all cards
* Autoshuffling
    * When reviewing, the shuffler will automatically shuffle using a specified method. This method can be changed using the [config](#Configuration).

# Usage
## Custom Menu Buttons
Using the custom menu button, you can control CloveShuffler's functionality.

<p align="center">
    <img src='https://raw.githubusercontent.com/m-riley04/CloveShuffler/main/assets/menubar.JPG' width='300'>
</p>

## Tagging
If you only want CloveShuffler to shuffle specific cards, you can tag your cards with the word "shuffle".
<p align="center">
    <img src='https://github.com/m-riley04/CloveShuffler/blob/main/assets/tag.JPG?raw=true' width='400' style="padding:50px">
</p>

> # --PLEASE NOTE--
> The [autoshuffler's default shuffling method](https://github.com/m-riley04/CloveShuffler/blob/main/config.md#autoshuffle_method) is every tagged card within the current deck. This means that by default, if there are no tagged cards in the current deck, nothing will be shuffled. Details on how to change the default shuffling method will be discussed in the next section.

## Configuration
In short, if you want to change the configuration, simply go to your addons panel in the Tools/Add-Ons menu option, select "CloveShuffler," and then click the "Config" button.

Configuration details can be found extensively in the [configuration documentation](https://github.com/m-riley04/CloveShuffler/blob/main/config.md), which is also shown in the Add-On menu.

# Installation
1. Open your installation of Anki
2. Navigate with the menu bar to "Tools/Add-ons" and select it
3. From here, you have a few options
    - Click "Get Add-ons" if you have the add-on code
    - Click "Install from file..." if you have downloaded the .zip or .ankiaddon file from the [GitHub's releases](https://github.com/m-riley04/CloveShuffler/releases)
    - Click "View Files" if you have a regular folder with the add-on's files inside, then drag the folder into the "addons21" folder
4. (Optional) Restart Anki

# Technical Specifications
* Anki Version:     v23.12.1
* Python Version:   v3.12.0