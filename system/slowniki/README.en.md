# Dictionaries

In this directory are gathered dictionaries for PSS. They are grouped into several levels (pol. poziom).
In order to follow the coursebook you'd need dictionaries from level 0 and "robocze" directory.

*Warning - directory "robocze" is in use only until the publication of all planned level 0 dictionaries and will be changing. You always have to check for the newest version*

## How to use
In order to use the dictionaries with Plover software, you have to:
1. Download the dictionary
2. Move it to your designated dictionary directory (optional)
3. In Plover, choose "Add dictionary" - big green plus at the bottom of the window, and then "Load dictionary"
4. Pick downloaded dictionary

It is advised to keep dictionary hierarchy the way it is shown below.

## Dictionary hierarchy
*Information below is important for people makeing new dictionaries*
In the process of making new dictionaries it it advised to avoid conflicts with dictionaries at equal or lower levels.
In case of the conflict, the dictionary with lower level is more important.
All learning materials regarding PSS assume usage of level 0 dictionaries. Advanced materials assume level 1.

### Level 0
Level 0 consists of dictionaries neccessary for the most basic usage of PSS.
Level 0 includes:
* pss-rdzenie-bazowe.json - word roots get from list of the 10000 the most frequently used polish words by Jerzy Kazojć, as well as some other roots present in frequent, common words
* pss-przyrostki-bazowe.json - simple grammatical and morphological suffixes based on Kazojć's list
* pss-przedrostki-bazowe.json - simple prefixes based on Kazojć's list
* pss-skroty-gramatyczne.json - pronouns (including simplified versions of complex pronouns), conjunctions, particles, prepositions
* pss-interpunkcja.json - interpunction and text formatting
* pss-komputer.json - emulation of Polish QUERTY keyboard
* pss-plover.json - usage of Plover software

### Level 1
Level 1 consists of dictionaries rendered to be neccessary to use PSS efficiently, but do not expand vocabulary from level 0.
Level 1 includes:
* przedrostki-zlozone.json - practical compunding of multiple simple prefixes into one
* przyrostki-zlozone.json - complex grammatical suffixes, not compounded with morphological suffixes
* przyrostki-rozszerzone.json - the most common complex suffixes consisting of morphological and complex grammatical suffixes
* skrocenia.json - one-chord briefs for the most common words and word groups

### Level 2
Level 2 consists of dictionaries with words that are less common, but are still part of standard Polish variant.
Level 2 includes:
* common proper nouns - Polish names, countries, capitals, voivodships and their capitals, international organizations
* theme dictionaries - i.e. law, court, programming, medicine

### Level 3
Level 3 consists of dictionaries with words that may not belong to standard Polish language variation.
Level 3 includes:
* not polonised loanwords
* dialectal words
* slang words
* cities and town names not included in Level 2 - due to complexity

## State of work
* level 0 - technical dictionaries finished, work on list of 10000 words in progress
* level 1 - work on list of 10000 words in progress, in order to extract suffixes, prefixes and creating briefs
* level 2 - not started
* level 3 - not started
