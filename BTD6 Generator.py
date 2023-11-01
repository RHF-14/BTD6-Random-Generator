import PySimpleGUI as gui
from random import choice

#----------------------------------#
#   TUPLES IN ORDER SHOWN IN GAME  #
#----------------------------------#

# tuple of heroes 
heroes = ("Quincy", "Gwendolin", "Striker Jones", "Obyn Greenfoot", "Geraldo", "Captain Churchill", "Benjamin", "Ezili", "Pat Fusty", "Adora", "Admiral Brickell ", "Etienne", "Sauda", "Psi")

# tuple of monkeys
allMonkeys = ("Dart Monkey", "Boomerang Monkey", "Bomb Shooter", "Tack Shooter", "Ice Monkey", "Glue Gunner", "Sniper Monkey", "Monkey Sub", "Monkey Buccaneer", "Monkey Ace", "Heli Pilot", "Mortar Monkey","Dartling Gunner", "Wizard Monkey", "Super Monkey", "Ninja Monkey", "Alchemist", "Druid", "Banana Farm", "Spike Factory", "Monkey Village", "Engineer Monkey", "Beast Handler")
primaryMonkeys = ("Dart Monkey", "Boomerang Monkey", "Bomb Shooter", "Tack Shooter", "Ice Monkey", "Glue Gunner")
militaryMonkeys = ("Sniper Monkey", "Monkey Sub", "Monkey Buccaneer", "Monkey Ace", "Heli Pilot", "Mortar Monkey","Dartling Gunner")
magicMonkeys = ("Wizard Monkey", "Super Monkey", "Ninja Monkey", "Alchemist", "Druid")

# tuple of modes
easyModes = ("Easy", "Primary Monkeys Only", "Deflation")
mediumModes = ("Medium", "Military Monkeys Only", "Apopalypse", "Reverse")
hardModes = ("Hard", "Magic Monkeys Only", "Double HP Moabs", "Half Cash", "Alternate Bloons Rounds", "Impoppable")

# tuple of maps
beginnerMaps = ("Monkey Meadow", "Tree Stump", "Town Center", "Middle of the Road", "One Two Tree", "Scrapyard", "The Cabin", "Resort", "Skates", "Lotus Island", "Candy Falls", "Winter Park", "Carved", "Park Path", "Alpine Run", "Frozen Over", "In The Loop", "Cubism", "Four Circles", "Hedge", "End Of The Road", "Logs")
intermediateMaps = ("Water Park", "Polyphemus", "Covered Garden", "Quarry", "Quiet Street", "Bloonarius Prime", "Balance", "Encrypted", "Bazaar", "Adora's Temple", "Spring Spring", "KartsNDarts", "Moon Landing", "Haunted", "Downstream", "Firing Range", "Cracked", "Streambed", "Chutes", "Rake", "Spice Islands")
advancedMaps = ("Dark Path", "Erosion", "Midnight Mansion", "Sunken Columns", "X Factor", "Mesa", "Geared", "Spillway", "Cargo", "Pat's Pond", "Peninsula", "High Finance", "Another Brick", "Off The Coast", "Cornfield", "Underground")
expertMaps = ("Dark Dungeons", "Sanctuary", "Ravine", "Flooded Valley", "Infernal", "Bloody Puddles", "Workshop", "Quad", "Dark Castle", "Muddy Puddles", "#Ouch")

#---------------#
#   FUNCTIONS   #
#---------------#

def generateHeroes(mode): # picks random hero
    if mode == "CHIMPS":
        heroChoice = choice(heroes)
        while(heroChoice == "Benjamin"):
            heroChoice = choice(heroes)
    else:
        heroChoice = choice(heroes)
    return heroChoice

def generateMonkeys(numMonkeys, mode): # generates one set of random monkeys, returns in an array
    
    # ensures that if no other gamemode is selected, the most restrictive is default
    if mode == None:
        mode = "CHIMPS"
    
    returnArray = []
    
    if(mode == "Primary Monkeys Only"): #picks from primary monkeys only
        for j in range(1, (numMonkeys + 1)):
            returnArray.append(choice(primaryMonkeys))
    elif(mode == "Military Monkeys Only"): #picks from military monkeys only
        for j in range(1, (numMonkeys + 1)):
            returnArray.append(choice(militaryMonkeys))
    elif(mode == "Magic Monkeys Only"): #picks from magic moneys only
        for j in range(1, (numMonkeys + 1)):
            returnArray.append(choice(magicMonkeys))
    elif(mode == "CHIMPS"): #removes banana farm since chimps does not allow it
        for j in range(1, (numMonkeys + 1)):
            monkeyChoice = choice(allMonkeys)
            while (monkeyChoice == "Banana Farm"): #this while  ensures that there are no banana farms in selected monkeys
                monkeyChoice = choice(allMonkeys)
            returnArray.append(monkeyChoice)
    else: #creates monkeys based on no monkey restrictions
        for j in range(1, (numMonkeys + 1)):
            returnArray.append(choice(allMonkeys))
    return returnArray
            
def generateMap(mapSelect): # picks random map based on choice
    if(mapSelect == 1): #picks random map based on beginner maps
        mapPool = beginnerMaps
        map = choice(mapPool)
        return map
    elif(mapSelect == 2): #adds beginner and intermediate maps except expert maps into 1 pool, picks based on that
        mapPool = intermediateMaps
        map = choice(mapPool)
        return map
    elif(mapSelect == 3): #adds all maps except expert maps into 1 pool, picks based on that
        mapPool = advancedMaps
        map = choice(mapPool)
        return map
    elif(mapSelect == 4): #adds all maps into 1 pool, does not allow beginner maps, or expert maps
        mapPool = expertMaps
        map = choice(mapPool)
        return map   

def generateMode(difficulty): # generates random mode based of difficulty selected
    if(difficulty == 1):
        return (choice(easyModes))
    elif(difficulty == 2):
        return (choice(mediumModes))
    elif(difficulty == 3):
        return (choice(hardModes))
    elif(difficulty == 4):
        return "CHIMPS"

#------------------------------#
#   GRAPHICAL USER INTERFACE   #
#------------------------------#

# color scheme
gui.theme('DarkGrey14')

# top columns
options_column = [
    [gui.Text("Monkeys per Player:"), gui.Slider(range=(1, 5), default_value=3, enable_events=True, orientation='horizontal', key='-MONKEYS-')],
    [gui.Text("Map:", size=7), gui.Button("Beginner", size=10), gui.Button("Intermediate", size=10), gui.Button("Advanced", size=10), gui.Button("Expert", size=10)],
    [gui.Text("Difficulty: ", size=7), gui.Button("Easy", size=10), gui.Button("Medium", size=10), gui.Button("Hard", size=10), gui.Button("CHIMPS", size=10) ]
]

map_mode_column = [
    [gui.Text("Map:", size=5), gui.Text(key="-MAP-")],
    [gui.Text("Mode:", size=5), gui.Text(key="-MODE-")]
]

# final layout
layout = [
    [gui.Column(options_column), gui.VSeparator(pad=(0,0)), gui.Column(map_mode_column)],
    [gui.HorizontalSeparator(pad=(0,0))],
    [gui.Sizer(0,10)],
    [gui.Text("Players:", size=(14), pad=(0,0)),gui.Text("Heroes:", size=(13)),gui.Text("Monkeys:", size=(15))],
    [gui.HSeparator(pad=(0,0))],
    [gui.Button("Gen Player 1", size=(12)), gui.VSeparator(pad=(0,0)), gui.Text(key="-HERO1-", size=(13)), gui.VSeparator(pad=(0,0)), gui.Text(key="-MONKEY1-", expand_x=True)],
    [gui.Button("Gen Player 2", size=(12)), gui.VSeparator(pad=(0,0)), gui.Text(key="-HERO2-", size=(13)), gui.VSeparator(pad=(0,0)), gui.Text(key="-MONKEY2-", expand_x=True)],
    [gui.Button("Gen Player 3", size=(12)), gui.VSeparator(pad=(0,0)), gui.Text(key="-HERO3-", size=(13)), gui.VSeparator(pad=(0,0)), gui.Text(key="-MONKEY3-", expand_x=True)],
    [gui.Button("Gen Player 4", size=(12)), gui.VSeparator(pad=(0,0)), gui.Text(key="-HERO4-", size=(13)), gui.VSeparator(pad=(0,0)), gui.Text(key="-MONKEY4-", expand_x=True)],
    [gui.HSeparator(pad=(0,0))],
    [gui.Sizer(0,5)],
    [gui.Button("Exit", size=(4)), gui.Button("Clear", size=(6))]
]

# default game mode is most restrictive for monkey and hero generation if one is not picked
gameMode = "CHIMPS"

# creation of window
window = gui.Window("BTD6 Monkey Generator", layout, size=(840, 340), icon=r"C:\Users\aiden\OneDrive\Visual Studio Code\z - Executables\BTD6 Generator\ParagonIcon.ico")


##############
# EVENT LOOP #
##############

while True:
    event, values = window.read()
    
    # pulls numMonkeys from the slider element
    try: # this try is here because the program throws an error when exiting using the 'X'
        numMonkeys = int(values["-MONKEYS-"])
    except: # simply just ignores the error since it doesn't affect normal operation of code
        pass

    # mode generation
    if event == "Easy":
        gameMode=generateMode(1)
        window["-MODE-"].update(gameMode)
    if event == "Medium":
        gameMode=generateMode(2)
        window["-MODE-"].update(gameMode)
    if event == "Hard":
        gameMode=generateMode(3)
        window["-MODE-"].update(gameMode)  
    if event == "CHIMPS":
        gameMode="CHIMPS"
        window["-MODE-"].update(gameMode)
        
    # map generation
    if event == "Beginner":
        gameMap=generateMap(1)
        window["-MAP-"].update(gameMap)
    if event == "Intermediate":
        gameMap=generateMap(2)
        window["-MAP-"].update(gameMap)
    if event == "Advanced":
        gameMap=generateMap(3)
        window["-MAP-"].update(gameMap)  
    if event == "Expert":
        gameMap=generateMap(4)
        window["-MAP-"].update(gameMap)

    # generate player 1 hero and monkeys
    if event == "Gen Player 1":
        monkeysArray = generateMonkeys(numMonkeys, gameMode)
        strLit = ""
        for i in range(0, len(monkeysArray)-1):
            strLit += monkeysArray[i] + ", "
        strLit += monkeysArray[len(monkeysArray)-1]
        window["-MONKEY1-"].update(strLit)
        
        playerHero = generateHeroes(gameMode)
        window["-HERO1-"].update(playerHero)
        
    # generate player 2 hero and monkeys
    if event == "Gen Player 2":
        monkeysArray = generateMonkeys(numMonkeys, gameMode)
        strLit = ""
        for i in range(0, len(monkeysArray)-1):
            strLit += monkeysArray[i] + ", "
        strLit += monkeysArray[len(monkeysArray)-1]
        window["-MONKEY2-"].update(strLit)
        
        playerHero = generateHeroes(gameMode)
        window["-HERO2-"].update(playerHero)
        
    # generate player 3 hero and monkeys
    if event == "Gen Player 3":
        monkeysArray = generateMonkeys(numMonkeys, gameMode)
        strLit = ""
        for i in range(0, len(monkeysArray)-1):
            strLit += monkeysArray[i] + ", "
        strLit += monkeysArray[len(monkeysArray)-1]
        window["-MONKEY3-"].update(strLit)
        
        playerHero = generateHeroes(gameMode)
        window["-HERO3-"].update(playerHero)
    
    # generate player 4 hero and monkeys
    if event == "Gen Player 4":
        monkeysArray = generateMonkeys(numMonkeys, gameMode)
        strLit = ""
        for i in range(0, len(monkeysArray)-1):
            strLit += monkeysArray[i] + ", "
        strLit += monkeysArray[len(monkeysArray)-1]
        window["-MONKEY4-"].update(strLit)
        
        playerHero = generateHeroes(gameMode)
        window["-HERO4-"].update(playerHero)
        
    # clears hero and monkey choice when clear button is pressed
    if event == "Clear":
        window["-MAP-"].update("")
        window["-MODE-"].update("")
        window["-HERO1-"].update("")
        window["-HERO2-"].update("")
        window["-HERO3-"].update("")
        window["-HERO4-"].update("")
        window["-MONKEY1-"].update("")
        window["-MONKEY2-"].update("")
        window["-MONKEY3-"].update("")
        window["-MONKEY4-"].update("")
        gameMode = "CHIMPS"
    
    #closing window
    if event == "Exit" or event == gui.WIN_CLOSED:
        break
# end while true

#ends the program
window.close()